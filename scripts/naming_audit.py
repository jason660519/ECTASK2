#!/usr/bin/env python3
"""Project naming and file-management audit utility.

Usage examples:
  python3 scripts/naming_audit.py
  python3 scripts/naming_audit.py --root . --json
  python3 scripts/naming_audit.py --write-report naming_audit_report.md
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


IGNORE_DIRS = {
    ".git",
    ".venv",
    ".venv39",
    "node_modules",
    "dist",
    "build",
    "__pycache__",
}

# Existing project files that are intentionally non-ASCII or exception names.
FILE_NAME_EXCEPTIONS = {
    ".gitignore",
    "SKILL.md",
}

BANNED_TOKENS = {
    "new",
    "latest",
    "fixed",
    "use_this",
    "v2_final_final",
}

STATUS_TOKENS = {"draft", "final", "orig", "formatted", "archive", "clean", "submission"}

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SNAKE_CASE_RE = re.compile(r"^[a-z0-9_]+$")
KEBAB_CASE_RE = re.compile(r"^[a-z0-9-]+$")


@dataclass
class Finding:
    level: str
    kind: str
    path: str
    message: str
    suggestion: str = ""


def iter_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        yield path


def normalize_name(base_name: str) -> str:
    stem, dot, suffix = base_name.rpartition(".")
    if dot == "":
        stem = base_name
        suffix = ""

    normalized = stem.strip().lower()
    normalized = re.sub(r"[^a-z0-9]+", "_", normalized)
    normalized = re.sub(r"_+", "_", normalized).strip("_")
    if not normalized:
        normalized = "file"

    if suffix:
        return f"{normalized}.{suffix.lower()}"
    return normalized


def check_name(path: Path, root: Path) -> list[Finding]:
    findings: list[Finding] = []
    base_name = path.name

    if base_name in FILE_NAME_EXCEPTIONS:
        return findings

    stem = path.stem
    rel = str(path.relative_to(root))
    in_claude_commands = ".claude/commands/" in rel.replace("\\", "/")

    if any(ch.isupper() for ch in base_name):
        findings.append(
            Finding(
                level="warning",
                kind="uppercase",
                path=rel,
                message="Filename contains uppercase letters.",
                suggestion=normalize_name(base_name),
            )
        )

    if " " in base_name:
        findings.append(
            Finding(
                level="warning",
                kind="space",
                path=rel,
                message="Filename contains spaces.",
                suggestion=normalize_name(base_name),
            )
        )

    if not all(ord(ch) < 128 for ch in base_name):
        findings.append(
            Finding(
                level="info",
                kind="non_ascii",
                path=rel,
                message="Filename uses non-ASCII characters.",
                suggestion="",
            )
        )

    style_ok = bool(SNAKE_CASE_RE.match(stem))
    if in_claude_commands:
        # Existing command files use kebab-case by convention.
        style_ok = bool(KEBAB_CASE_RE.match(stem))

    if not style_ok:
        findings.append(
            Finding(
                level="warning",
                kind="style",
                path=rel,
                message=(
                    "Filename stem is not valid style for this location "
                    "(snake_case by default; kebab-case allowed in .claude/commands)."
                ),
                suggestion=normalize_name(base_name),
            )
        )

    lower_stem = stem.lower()
    for token in BANNED_TOKENS:
        if token in lower_stem:
            findings.append(
                Finding(
                    level="error",
                    kind="banned_token",
                    path=rel,
                    message=f"Filename contains banned token '{token}'.",
                    suggestion=normalize_name(base_name),
                )
            )

    if path.suffix == ".md":
        parts = lower_stem.split("_")
        if len(parts) >= 2 and parts[-1] not in STATUS_TOKENS and rel != "index.md":
            findings.append(
                Finding(
                    level="info",
                    kind="status_hint",
                    path=rel,
                    message=(
                        "Consider adding a status suffix (draft/final/orig/formatted/archive/clean/submission) "
                        "if this file represents a lifecycle state."
                    ),
                    suggestion="",
                )
            )

    return findings


def check_index_links(index_path: Path, root: Path) -> list[Finding]:
    findings: list[Finding] = []
    if not index_path.exists():
        return [
            Finding(
                level="warning",
                kind="index_missing",
                path=str(index_path.relative_to(root)),
                message="index.md not found; skip link consistency check.",
                suggestion="",
            )
        ]

    content = index_path.read_text(encoding="utf-8", errors="replace")
    for match in MARKDOWN_LINK_RE.finditer(content):
        target = match.group(1).strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_no_anchor = target.split("#", 1)[0]
        if not target_no_anchor:
            continue
        resolved = (index_path.parent / target_no_anchor).resolve()
        if not resolved.exists():
            findings.append(
                Finding(
                    level="error",
                    kind="broken_link",
                    path=str(index_path.relative_to(root)),
                    message=f"Broken link target: {target}",
                    suggestion="Update link or create target file.",
                )
            )
    return findings


def format_markdown(findings: list[Finding], root: Path) -> str:
    lines = [
        "# Naming Audit Report",
        "",
        f"- Root: {root}",
        f"- Total findings: {len(findings)}",
        "",
    ]

    if not findings:
        lines.append("No issues found.")
        return "\n".join(lines)

    grouped = {"error": [], "warning": [], "info": []}
    for item in findings:
        grouped.setdefault(item.level, []).append(item)

    for level in ("error", "warning", "info"):
        items = grouped.get(level) or []
        lines.append(f"## {level.capitalize()} ({len(items)})")
        lines.append("")
        if not items:
            lines.append("- None")
            lines.append("")
            continue
        for f in items:
            detail = f"- [{f.kind}] {f.path}: {f.message}"
            if f.suggestion:
                detail += f" Suggested: {f.suggestion}"
            lines.append(detail)
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit naming and file management consistency.")
    parser.add_argument("--root", default=".", help="Workspace root path.")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output findings in JSON.")
    parser.add_argument("--write-report", default="", help="Write markdown report to this file path.")
    parser.add_argument("--index", default="index.md", help="Relative path to index file for link checks.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    findings: list[Finding] = []

    for file_path in iter_files(root):
        findings.extend(check_name(file_path, root))

    findings.extend(check_index_links((root / args.index).resolve(), root))

    findings.sort(key=lambda x: (x.level, x.path, x.kind))

    if args.write_report:
        report_path = (root / args.write_report).resolve()
        report_path.write_text(format_markdown(findings, root), encoding="utf-8")

    if args.as_json:
        print(json.dumps([asdict(f) for f in findings], ensure_ascii=False, indent=2))
    else:
        errors = sum(1 for f in findings if f.level == "error")
        warnings = sum(1 for f in findings if f.level == "warning")
        infos = sum(1 for f in findings if f.level == "info")
        print(f"Findings: errors={errors}, warnings={warnings}, info={infos}")
        for f in findings:
            suffix = f" | suggestion: {f.suggestion}" if f.suggestion else ""
            print(f"[{f.level}] {f.kind} | {f.path} | {f.message}{suffix}")

    return 1 if any(f.level == "error" for f in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
