import sys

ch_fi = sys.argv[2] if len(sys.argv) == 3 else "CHANGELOG.md"
try:
    tag = sys.argv[1]
except:
    print("Usage create_changelog.py <tag> [CHANGELOG_FILE]", file=sys.stderr)
    exit(1)
print("# Changelog\n")
with open(ch_fi, "r") as fr:
    has_started = False
    for line in fr.readlines():
        if line.startswith(f"## [{tag}]"):
            print(line.rstrip())
            has_started = True
        elif has_started and line.startswith(f"##"):
            break
        elif has_started:
            print(line.rstrip())

