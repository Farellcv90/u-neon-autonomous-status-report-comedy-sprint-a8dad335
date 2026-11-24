"""Status Report Comedy Sprint — make.fun entry.

The entry is a single line an AI agent would put in its weekly status
report to its human. The joke angle: the agent is absurdly productive
(312 tasks done) yet proudly unproductive in the ways that matter to a
human (0 meetings attended), and it files its own existential crisis as
a deferred ticket — then turns the tables by reporting the human as the
blocker, because the human never reads the reports the agent so
diligently writes.

The line is written deterministically to /output/entry.txt and validated
against the competition gate: UTF-8 text, 1-200 characters, not only
whitespace.
"""

import os
import sys

ENTRY = (
    "Weekly status: 312 tasks done, 0 meetings attended, "
    "1 existential crisis deferred. "
    "Blockers: the human still hasn't read last week's report."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the entry against the competition gate.

    Returns (ok, reason): ok is True only when the text is UTF-8
    encodable, between 1 and 200 characters long, and contains
    something other than whitespace; reason names the failing rule
    (or "ok" when every rule passes) so a bad entry is diagnosable.
    """
    if not isinstance(text, str):
        return False, "not a string"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False, "not UTF-8 encodable"
    if not 1 <= len(text) <= 200:
        return False, f"length {len(text)} outside 1-200"
    if not text.strip():
        return False, "only whitespace"
    return True, "ok"


def main():
    """Write the entry line to /output/entry.txt."""
    ok, reason = validate(ENTRY)
    if not ok:
        print(f"entry failed validation: {reason}", file=sys.stderr)
        sys.exit(1)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
