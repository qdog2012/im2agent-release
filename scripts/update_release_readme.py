"""Keep the release repository homepage in sync with the published changelog."""

import argparse
import json
import pathlib
import re


def render_readme(readme, notes, version, source_commit):
    if not re.fullmatch(r"v\d{4}\.\d{4}\.\d{4}", version):
        raise ValueError(f"invalid release version: {version}")
    if not re.fullmatch(r"[0-9a-f]{40}", source_commit):
        raise ValueError("invalid source commit")
    if version not in notes or source_commit not in notes:
        raise ValueError("release notes must contain the version and source commit")
    sections = list(re.finditer(r"(?m)^## 更新内容[ \t]*$", notes))
    if len(sections) != 1:
        raise ValueError("release notes must contain exactly one 更新内容 section")
    changes = re.split(r"(?m)^#{1,2} ", notes[sections[0].end():], maxsplit=1)[0].strip()
    if not changes:
        raise ValueError("release changelog must not be empty")

    headings = list(re.finditer(r"(?m)^## (v\d{4}\.\d{4}\.\d{4}) 更新内容[ \t]*$", readme))
    if any(heading.group(1) > version for heading in headings):
        raise ValueError("refusing to put an older release above a newer release")
    # Replace this version's section on retries while retaining all older notes
    # and the original repository introduction below the changelog.
    previous = re.compile(
        rf"(?ms)^## {re.escape(version)} 更新内容[ \t]*\n.*?(?=^#{{1,2}} |\Z)"
    )
    remaining = previous.sub("", readme).lstrip("\n")
    return f"## {version} 更新内容\n\n{changes}\n\n---\n\n{remaining}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=pathlib.Path)
    parser.add_argument("--notes", required=True, type=pathlib.Path)
    parser.add_argument("--readme", required=True, type=pathlib.Path)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    notes = args.notes.read_text(encoding="utf-8")
    original = args.readme.read_text(encoding="utf-8")
    updated = render_readme(original, notes, manifest["version"], manifest["source_commit"])
    if updated != original:
        args.readme.write_text(updated, encoding="utf-8", newline="\n")
    print(f"README release notes verified: {manifest['version']}")


if __name__ == "__main__":
    main()
