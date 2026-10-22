#!/usr/bin/env python3
"""Condense a Claude Code session transcript into a readable Markdown file.

Claude Code saves every session as JSONL under ~/.claude/projects/<folder>/.
Those files are large (every tool result is in there) and hard to read. This
keeps what the log needs: your prompts verbatim, the AI's replies, a one-line
note per tool call, errors, interruptions, rejected tool calls, and real
timestamps, including the gaps where you were reading or thinking.

Usage:
    python transcript.py                   # latest session for the current folder
    python transcript.py <folder>          # latest session for that working folder
    python transcript.py <file.jsonl>      # a specific session
    python transcript.py --list [<folder>] # list sessions, newest first
    python transcript.py ... -o transcript.md
    python transcript.py ... --inputs 400  # also show what the AI wrote, clipped

Standard library only. Python 3.8+.
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

PROJECTS = Path.home() / ".claude" / "projects"

# Wrapper tags Claude Code adds around prompts. Not something the human typed.
NOISE_TAGS = re.compile(
    r"<(system-reminder|ide_selection|ide_opened_file|ide_diagnostics|"
    r"local-command-caveat|local-command-stdout|local-command-stderr|"
    r"command-message|command-args|user-memory-input)>.*?</\1>",
    re.S,
)
COMMAND_NAME = re.compile(r"<command-name>(.*?)</command-name>", re.S)
COMMAND_ARGS = re.compile(r"<command-args>(.*?)</command-args>", re.S)
INTERRUPT = re.compile(r"^\[Request interrupted by user[^\]]*\]$")
REJECTED = "The user doesn't want to proceed with this tool use"
REJECT_REASON = re.compile(r"reason for the rejection:\s*(.*)", re.S)


def project_dir_for(folder):
    """Claude Code names each project folder after its path, with every
    non-alphanumeric character replaced by '-'. Drive-letter case varies."""
    slug = re.sub(r"[^A-Za-z0-9]", "-", str(Path(folder).resolve()))
    if PROJECTS.is_dir():
        for d in PROJECTS.iterdir():
            if d.is_dir() and d.name.lower() == slug.lower():
                return d
    sys.exit(f"No Claude Code transcripts found for {folder}\n(looked for {PROJECTS / slug})")


def sessions_in(project_dir):
    files = [f for f in project_dir.glob("*.jsonl") if f.stat().st_size > 0]
    return sorted(files, key=lambda f: f.stat().st_mtime, reverse=True)


def parse_time(ts):
    if not ts:
        return None
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone()
    except ValueError:
        return None


def clip(text, limit):
    text = text.strip()
    if limit and len(text) > limit:
        return text[:limit].rstrip() + f" […{len(text) - limit} more chars]"
    return text


def one_line(text, limit=120):
    return clip(" ".join(str(text).split()), limit)


def blocks(content):
    if isinstance(content, str):
        return [{"type": "text", "text": content}]
    return content if isinstance(content, list) else []


def result_text(content):
    if isinstance(content, str):
        return content
    return " ".join(b.get("text", "") for b in blocks(content) if b.get("type") == "text")


def tool_payload(inp, limit):
    """The longest string in a tool call's input: usually what the AI wrote."""
    if not limit or not isinstance(inp, dict):
        return ""
    strings = [v for v in inp.values() if isinstance(v, str)]
    if not strings:
        strings = [json.dumps(inp, ensure_ascii=False)]
    longest = max(strings, key=len)
    return clip(longest, limit) if len(longest) > 100 else ""


def describe_tool(name, inp):
    """One line per tool call: enough to see what the AI did, not the payload."""
    if not isinstance(inp, dict):
        return name
    if inp.get("description"):
        detail = inp["description"]
    elif inp.get("file_path") or inp.get("path") or inp.get("notebook_path"):
        detail = inp.get("file_path") or inp.get("path") or inp.get("notebook_path")
    elif inp.get("command"):
        detail = inp["command"]
    elif inp.get("pattern"):
        detail = inp["pattern"]
    else:
        detail = next((v for v in inp.values() if isinstance(v, str)), "")
    return f"{name}: {one_line(detail, 100)}" if detail else name


def events(path, input_chars=0):
    """Yield (time, kind, text) in transcript order."""
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if rec.get("isSidechain"):
                continue  # subagent traffic, not the conversation
            t = parse_time(rec.get("timestamp"))
            kind = rec.get("type")

            if kind == "system" and rec.get("subtype") == "compact_boundary":
                yield t, "compact", ""
                continue

            if kind == "attachment":
                att = rec.get("attachment") or {}
                if att.get("type") == "queued_command" and (att.get("origin") or {}).get("kind") == "human":
                    text = result_text(att.get("prompt", ""))
                    if text.strip():
                        yield t, "midturn", text
                continue

            msg = rec.get("message") or {}
            if kind == "user":
                if rec.get("isCompactSummary"):
                    yield t, "compact", ""
                    continue
                if rec.get("isMeta"):
                    continue
                for b in blocks(msg.get("content")):
                    if b.get("type") == "tool_result":
                        text = result_text(b.get("content"))
                        if text.startswith(REJECTED):
                            reason = REJECT_REASON.search(text)
                            yield t, "rejected", reason.group(1) if reason else ""
                        elif b.get("is_error"):
                            yield t, "error", text
                    elif b.get("type") == "text":
                        raw = b.get("text", "")
                        cmd = COMMAND_NAME.search(raw)
                        if cmd:
                            args = COMMAND_ARGS.search(raw)
                            yield t, "command", f"{cmd.group(1)} {args.group(1) if args else ''}".strip()
                            continue
                        text = NOISE_TAGS.sub("", raw).strip()
                        if not text:
                            continue
                        if INTERRUPT.match(text):
                            yield t, "interrupt", ""
                        else:
                            yield t, "prompt", text
                    elif b.get("type") == "image":
                        yield t, "prompt", "[image attached]"

            elif kind == "assistant":
                for b in blocks(msg.get("content")):
                    if b.get("type") == "text" and b.get("text", "").strip():
                        yield t, "reply", b["text"]
                    elif b.get("type") == "tool_use":
                        line = describe_tool(b.get("name", "tool"), b.get("input"))
                        payload = tool_payload(b.get("input"), input_chars)
                        if payload:
                            line += "\n\n  ```\n" + "\n".join("  " + l for l in payload.splitlines()) + "\n  ```\n"
                        yield t, "tool", line


def fmt(t):
    return t.strftime("%H:%M:%S") if t else "--:--:--"


def minutes(seconds):
    return f"{seconds / 60:.0f} min"


def render(path, max_reply, input_chars):
    evs = list(events(path, input_chars))
    timed = [t for t, _, _ in evs if t]
    if not timed:
        sys.exit(f"No conversation found in {path}")
    t0, t_end = timed[0], timed[-1]

    out, n_prompt, gap_total, last_ai = [], 0, 0.0, None
    n_correct = {"interrupt": 0, "rejected": 0, "midturn": 0}

    def stamp(t):
        el = int((t - t0).total_seconds()) if t else 0
        return f"{fmt(t)} · +{el // 3600}:{el // 60 % 60:02d}"

    for t, kind, text in evs:
        if kind in ("prompt", "midturn"):
            n_prompt += 1
            gap = ""
            # A mid-turn message arrives while the AI is still working, so it ends no gap.
            if kind == "prompt" and last_ai and t:
                secs = max(0.0, (t - last_ai).total_seconds())
                gap_total += secs
                gap = f" · {minutes(secs)} after the AI's last action" if secs >= 60 else ""
            label = "HUMAN, mid-turn (sent while the AI was working)" if kind == "midturn" else "HUMAN"
            if kind == "midturn":
                n_correct["midturn"] += 1
            out.append(f"\n### [{stamp(t)}] {label}, prompt {n_prompt}{gap}\n")
            out.append("\n".join("> " + l if l else ">" for l in text.strip().splitlines()) + "\n")
            last_ai = None
        elif kind == "reply":
            out.append(f"\n**[{fmt(t)}] AI:**\n\n{clip(text, max_reply)}\n")
            last_ai = t
        elif kind == "tool":
            out.append(f"- `{fmt(t)}` tool · {text}")
            last_ai = t
        elif kind == "error":
            out.append(f"- `{fmt(t)}` ✗ tool error · {one_line(text, 200)}")
            last_ai = t
        elif kind == "rejected":
            n_correct["rejected"] += 1
            reason = f": \"{one_line(text, 600)}\"" if text.strip() else ""
            out.append(f"\n**[{stamp(t)}] ⚠ HUMAN rejected the AI's tool call{reason}**\n")
            last_ai = None
        elif kind == "interrupt":
            n_correct["interrupt"] += 1
            out.append(f"\n**[{stamp(t)}] ⚠ HUMAN interrupted the AI**\n")
            last_ai = None
        elif kind == "command":
            out.append(f"\n*[{stamp(t)}] Human ran `{text}`*\n")
        elif kind == "compact":
            out.append(f"\n*[{fmt(t)}] — Context compacted: the AI's memory of the session was summarized here —*\n")

    elapsed = (t_end - t0).total_seconds()
    head = [
        f"# Transcript: {t0.strftime('%Y-%m-%d')} session",
        "",
        f"**Source:** `{Path(path).name}` (Claude Code)  ",
        f"**Clock:** {fmt(t0)} → {fmt(t_end)}, {minutes(elapsed)} elapsed  ",
        f"**Human prompts:** {n_prompt} · **Interruptions:** {n_correct['interrupt']} · "
        f"**Rejected tool calls:** {n_correct['rejected']} · **Mid-turn messages:** {n_correct['midturn']}  ",
        f"**Gaps:** about {minutes(gap_total)} between the AI finishing and the human's next prompt "
        f"(reading, reviewing, thinking, typing)",
        "",
        "> Condensed: tool results are omitted except errors, and tool calls are one line each"
        + (f", with what the AI wrote clipped to {input_chars} characters" if input_chars else "")
        + ". Review before sharing: transcripts can contain file contents, paths and secrets.",
    ]
    return "\n".join(head + out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", nargs="?", default=".", help="a .jsonl transcript, or a working folder (default: current folder)")
    ap.add_argument("-o", "--output", help="write to this file instead of the screen")
    ap.add_argument("--list", action="store_true", help="list sessions for the folder, newest first")
    ap.add_argument("--max-reply", type=int, default=3000, help="clip each AI reply to this many characters (0 = no limit)")
    ap.add_argument("--inputs", type=int, default=0, metavar="N",
                    help="also show what the AI wrote in each tool call (file contents, edits, commands), clipped to N characters")
    args = ap.parse_args()

    target = Path(args.target).expanduser()
    if target.suffix == ".jsonl":
        session = target
    else:
        found = sessions_in(project_dir_for(target))
        if not found:
            sys.exit("No sessions found.")
        if args.list:
            for f in found:
                first = next((x for _, k, x in events(f) if k == "prompt" or (k == "command" and x != "/clear")), "")
                when = datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
                print(f"{when}  {f}\n                  {one_line(first, 90)}")
            return
        session = found[0]

    text = render(session, args.max_reply, args.inputs)
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"Wrote {args.output} from {session}", file=sys.stderr)
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
