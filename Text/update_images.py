#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple


IMAGE_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".tif", ".tiff", ".bmp", ".pdf"
}

MARKDOWN_EXTENSIONS = {".md", ".markdown", ".myst"}
TAG_WIDTH = 15


@dataclass
class Stats:
    files_scanned: int = 0
    files_changed: int = 0
    refs_seen: int = 0
    refs_matched: int = 0
    refs_updated: int = 0
    refs_unchanged: int = 0
    refs_skipped: int = 0
    refs_ambiguous: int = 0
    refs_not_found: int = 0


@dataclass
class FileDebugLog:
    events: List[str] = field(default_factory=list)

    def add(
        self,
        tag: str,
        md_file: Path,
        kind: Optional[str] = None,
        original_ref: Optional[str] = None,
        found: Optional[Path] = None,
        rewritten: Optional[str] = None,
        extra: Optional[str] = None,
    ) -> None:
        parts = [f"[{tag:<{TAG_WIDTH}}]", str(md_file)]
        if kind is not None:
            parts.append(f"[{kind}]")
        if original_ref is not None:
            parts.append(original_ref)
        if found is not None:
            parts.append(f"-> matched: {found}")
        if rewritten is not None:
            parts.append(f"-> rewritten: {rewritten}")
        if extra is not None:
            parts.append(extra)
        self.events.append(" ".join(parts))

    def dump(self) -> None:
        for line in self.events:
            print(line)


def is_probably_external(path_str: str) -> bool:
    s = path_str.strip()
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", s)) or s.startswith("mailto:")


def split_target_and_title(target: str) -> Tuple[str, str]:
    s = target.strip()

    if s.startswith("<"):
        end = s.find(">")
        if end != -1:
            path_part = s[1:end]
            rest = s[end + 1 :]
            return path_part, rest
        return s, ""

    m = re.match(r"(\S+)(\s+.*)?$", s, flags=re.DOTALL)
    if not m:
        return s, ""
    path_part = m.group(1)
    rest = m.group(2) or ""
    return path_part, rest


def rebuild_target(path_str: str, trailing: str, use_angle_brackets: bool) -> str:
    if use_angle_brackets:
        return f"<{path_str}>{trailing}"
    return f"{path_str}{trailing}"


def build_image_index(new_image_root: Path) -> Tuple[Dict[str, List[Path]], Dict[str, List[Path]]]:
    by_name: Dict[str, List[Path]] = {}
    by_stem: Dict[str, List[Path]] = {}

    for p in new_image_root.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        by_name.setdefault(p.name.lower(), []).append(p)
        by_stem.setdefault(p.stem.lower(), []).append(p)

    return by_name, by_stem


def is_wildcard_ref(name: str) -> bool:
    return name.endswith(".*") or name.endswith(".\\*")


def wildcard_stem_from_name(name: str) -> str:
    if name.endswith(".\\*"):
        return name[:-3]
    if name.endswith(".*"):
        return name[:-2]
    return Path(name).stem


def split_ref_parts(ref: str) -> List[str]:
    return [p.lower() for p in Path(ref).parts]


def tail_match_score(ref_parts: List[str], candidate: Path) -> int:
    """
    Score how many trailing path components match between the original reference
    and the candidate path. Higher is better.
    """
    cand_parts = [p.lower() for p in candidate.parts]
    score = 0
    i = 1
    while i <= len(ref_parts) and i <= len(cand_parts):
        if ref_parts[-i] != cand_parts[-i]:
            break
        score += 1
        i += 1
    return score


def choose_best_candidate(
    original_ref: str,
    candidates: List[Path],
) -> Tuple[Optional[Path], str]:
    """
    Returns:
      (candidate, "ok") if a unique best candidate exists
      (None, "ambiguous") if several top candidates tie
      (None, "not_found") if no candidates exist
    """
    if not candidates:
        return None, "not_found"

    if len(candidates) == 1:
        return candidates[0], "ok"

    ref_parts = split_ref_parts(original_ref)
    scored = [(tail_match_score(ref_parts, c), c) for c in candidates]
    scored.sort(key=lambda x: x[0], reverse=True)

    best_score = scored[0][0]
    best = [c for score, c in scored if score == best_score]

    if len(best) == 1:
        return best[0], "ok"

    return None, "ambiguous"


def choose_match(
    original_ref: str,
    by_name: Dict[str, List[Path]],
    by_stem: Dict[str, List[Path]],
) -> Tuple[Optional[Path], str]:
    ref_path = Path(original_ref)
    fname = ref_path.name.lower()
    stem = ref_path.stem.lower()

    if is_wildcard_ref(fname):
        wildcard_stem = wildcard_stem_from_name(fname)
        candidates = by_stem.get(wildcard_stem, [])

        if not candidates:
            return None, "not_found"

        # Multiple files with same stem are fine if they all live in one directory.
        parent_dirs = {c.parent.resolve() for c in candidates}
        if len(parent_dirs) == 1:
            return sorted(candidates)[0], "wildcard"

        best, status = choose_best_candidate(original_ref, candidates)
        if best is not None:
            return best, "wildcard"
        return None, status

    candidates = by_name.get(fname, [])
    best, status = choose_best_candidate(original_ref, candidates)
    if best is not None:
        return best, "exact"
    if status == "ambiguous":
        return None, "ambiguous"

    candidates = by_stem.get(stem, [])
    best, status = choose_best_candidate(original_ref, candidates)
    if best is not None:
        return best, "stem"
    if status == "ambiguous":
        return None, "ambiguous"

    return None, "not_found"


def build_rewritten_ref(original_ref: str, found: Path, md_file: Path) -> str:
    original_name = Path(original_ref).name
    rel_parent = Path(os.path.relpath(found.parent, start=md_file.parent)).as_posix()
    rel_file = Path(os.path.relpath(found, start=md_file.parent)).as_posix()

    if original_name.endswith(".\\*"):
        if rel_parent == ".":
            return f"{found.stem}.\\*"
        return f"{rel_parent}/{found.stem}.\\*"

    if original_name.endswith(".*"):
        if rel_parent == ".":
            return f"{found.stem}.*"
        return f"{rel_parent}/{found.stem}.*"

    return rel_file


def rewrite_markdown_images(
    text: str,
    md_file: Path,
    by_name: Dict[str, List[Path]],
    by_stem: Dict[str, List[Path]],
    stats: Stats,
    log: FileDebugLog,
) -> str:
    pattern = re.compile(r"!\[((?:\\.|[^\]])*)\]\(([^)]+)\)")

    def repl(match: re.Match[str]) -> str:
        alt = match.group(1)
        raw_target = match.group(2)

        path_part, trailing = split_target_and_title(raw_target)
        stripped = path_part.strip()
        use_angle = stripped.startswith("<") and stripped.endswith(">")

        if use_angle:
            stripped = stripped[1:-1]

        stats.refs_seen += 1
        log.add("FOUND", md_file, "markdown-image", stripped)

        if is_probably_external(stripped):
            stats.refs_skipped += 1
            log.add("SKIP-EXTERNAL", md_file, "markdown-image", stripped)
            return match.group(0)

        found, reason = choose_match(stripped, by_name, by_stem)

        if not found:
            if reason == "ambiguous":
                stats.refs_ambiguous += 1
                log.add("AMBIGUOUS", md_file, "markdown-image", stripped)
            else:
                stats.refs_not_found += 1
                log.add("NOT-FOUND", md_file, "markdown-image", stripped)
            return match.group(0)

        stats.refs_matched += 1
        new_rel = build_rewritten_ref(stripped, found, md_file)
        new_target = rebuild_target(new_rel, trailing, use_angle_brackets=use_angle)
        new_markup = f"![{alt}]({new_target})"
        old_markup = match.group(0)

        if new_markup == old_markup:
            stats.refs_unchanged += 1
            log.add(
                "MATCH-UNCHANGED",
                md_file,
                "markdown-image",
                stripped,
                found=found,
                rewritten=new_target,
            )
            return old_markup

        stats.refs_updated += 1
        log.add(
            "MATCH-UPDATED",
            md_file,
            "markdown-image",
            stripped,
            found=found,
            rewritten=new_target,
        )
        return new_markup

    return pattern.sub(repl, text)


def rewrite_myst_directives(
    text: str,
    md_file: Path,
    by_name: Dict[str, List[Path]],
    by_stem: Dict[str, List[Path]],
    stats: Stats,
    log: FileDebugLog,
) -> str:
    lines = text.splitlines(keepends=True)
    open_pat = re.compile(
        r"""
        ^
        (?P<indent>[ \t]*)
        (?P<fence>:{3,}|`{3,})
        \{\s*(?P<kind>figure|image)\s*\}
        (?P<rest>[^\r\n]*)
        $
        """,
        re.VERBOSE,
    )

    for i, line in enumerate(lines):
        logical_line = line.rstrip("\r\n")

        if re.search(r"\{\s*(figure|image)\s*\}", logical_line):
            print(f"[RAW-FIGURE-LINE ] {md_file}:{i+1}: {logical_line}")

        m = open_pat.match(logical_line)
        if not m:
            continue

        rest = m.group("rest").strip()
        if not rest:
            continue

        m_arg = re.match(r"(?P<path><[^>]+>|\S+)(?P<tail>.*)$", rest)
        if not m_arg:
            continue

        raw_path = m_arg.group("path")
        tail = m_arg.group("tail")

        stripped = raw_path.strip()
        use_angle = stripped.startswith("<") and stripped.endswith(">")

        if use_angle:
            stripped = stripped[1:-1]

        kind = m.group("kind")
        stats.refs_seen += 1
        log.add("FOUND", md_file, kind, stripped)

        if is_probably_external(stripped):
            stats.refs_skipped += 1
            log.add("SKIP-EXTERNAL", md_file, kind, stripped)
            continue

        found, reason = choose_match(stripped, by_name, by_stem)

        if not found:
            if reason == "ambiguous":
                stats.refs_ambiguous += 1
                log.add("AMBIGUOUS", md_file, kind, stripped)
            else:
                stats.refs_not_found += 1
                log.add("NOT-FOUND", md_file, kind, stripped)
            continue

        stats.refs_matched += 1
        new_rel = build_rewritten_ref(stripped, found, md_file)
        new_arg = f"<{new_rel}>" if use_angle else new_rel
        new_line = f"{m.group('indent')}{m.group('fence')}{{{kind}}} {new_arg}{tail}"

        if line.endswith("\r\n"):
            new_line += "\r\n"
        elif line.endswith("\n"):
            new_line += "\n"

        if new_line == line:
            stats.refs_unchanged += 1
            log.add(
                "MATCH-UNCHANGED",
                md_file,
                kind,
                stripped,
                found=found,
                rewritten=new_arg,
            )
            continue

        lines[i] = new_line
        stats.refs_updated += 1
        log.add(
            "MATCH-UPDATED",
            md_file,
            kind,
            stripped,
            found=found,
            rewritten=new_arg,
        )

    return "".join(lines)


def process_markdown_file(
    md_file: Path,
    by_name: Dict[str, List[Path]],
    by_stem: Dict[str, List[Path]],
    stats: Stats,
    dry_run: bool,
) -> None:
    stats.files_scanned += 1
    original = md_file.read_text(encoding="utf-8")
    updated = original
    log = FileDebugLog()

    updated = rewrite_markdown_images(updated, md_file, by_name, by_stem, stats, log)
    updated = rewrite_myst_directives(updated, md_file, by_name, by_stem, stats, log)

    if updated != original:
        stats.files_changed += 1
        log.add("WRITE", md_file, extra="file content changed")
        if not dry_run:
            md_file.write_text(updated, encoding="utf-8")
    else:
        log.add("NOCHANGE", md_file, extra="file content unchanged")

    log.dump()


def iter_markdown_files(project_root: Path):
    for p in sorted(project_root.rglob("*")):
        if p.is_file() and p.suffix.lower() in MARKDOWN_EXTENSIONS:
            yield p


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Recursively scan Markdown/MyST files and replace image paths with "
            "relative paths pointing into a new image hierarchy. "
            "Supports wildcard extensions like 'file.*' and 'file.\\*', which are preserved."
        )
    )
    parser.add_argument(
        "new_image_root",
        type=Path,
        help="Path to the new image root folder.",
    )
    parser.add_argument(
        "-p",
        "--project-root",
        type=Path,
        default=Path.cwd(),
        help="Project root to scan recursively for markdown files. Default: current working directory.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not modify files, only report what would change.",
    )

    args = parser.parse_args()

    new_image_root = args.new_image_root.resolve()
    project_root = args.project_root.resolve()

    if not new_image_root.is_dir():
        print(f"Error: new image root does not exist or is not a directory: {new_image_root}", file=sys.stderr)
        return 2

    if not project_root.is_dir():
        print(f"Error: project root does not exist or is not a directory: {project_root}", file=sys.stderr)
        return 2

    by_name, by_stem = build_image_index(new_image_root)

    print(f"[{'INDEX':<{TAG_WIDTH}}] image root: {new_image_root}")
    print(f"[{'INDEX':<{TAG_WIDTH}}] indexed files: {sum(len(v) for v in by_name.values())}")
    print(f"[{'INDEX':<{TAG_WIDTH}}] unique exact names: {len(by_name)}")
    print(f"[{'INDEX':<{TAG_WIDTH}}] unique stems: {len(by_stem)}")

    stats = Stats()

    for md_file in iter_markdown_files(project_root):
        process_markdown_file(
            md_file=md_file,
            by_name=by_name,
            by_stem=by_stem,
            stats=stats,
            dry_run=args.dry_run,
        )

    print()
    print("Done.")
    print(f"Markdown files scanned : {stats.files_scanned}")
    print(f"Markdown files changed : {stats.files_changed}")
    print(f"Image refs seen        : {stats.refs_seen}")
    print(f"Image refs matched     : {stats.refs_matched}")
    print(f"Image refs updated     : {stats.refs_updated}")
    print(f"Image refs unchanged   : {stats.refs_unchanged}")
    print(f"Image refs skipped     : {stats.refs_skipped}")
    print(f"Ambiguous matches      : {stats.refs_ambiguous}")
    print(f"Not found              : {stats.refs_not_found}")
    print(f"Mode                   : {'dry-run' if args.dry_run else 'write'}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())