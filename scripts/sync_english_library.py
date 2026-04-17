#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path("/tmp/kaneliu120-pages-Pl4ZM3/site")
EN_SOURCE_DIR = Path(
    "/Users/kane/Documents/Obsidian Vault/00-战略中心/AI的人工替代全景分析/04-English-Industry-Library"
)
ZH_DOCS_DIR = ROOT / "_zh_docs"
EN_DOCS_DIR = ROOT / "_en_docs"


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text
    raw_fm = parts[0][4:]
    body = parts[1]
    data: dict[str, str] = {}
    for line in raw_fm.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        data[key.strip()] = value
    return data, body.lstrip()


def dump_frontmatter(data: dict[str, str]) -> str:
    ordered_keys = [
        "layout",
        "type",
        "title",
        "subtitle",
        "source_note",
        "created",
        "lang",
        "source_code",
        "source_file",
        "order_key",
        "tags",
        "target_keyword",
        "meta_description",
    ]
    lines = ["---"]
    for key in ordered_keys:
        if key not in data:
            continue
        value = data[key]
        if key == "tags":
            lines.append(f"{key}: {value}")
            continue
        escaped = value.replace('"', '\\"')
        lines.append(f'{key}: "{escaped}"')
    for key, value in data.items():
        if key in ordered_keys:
            continue
        escaped = value.replace('"', '\\"')
        lines.append(f'{key}: "{escaped}"')
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def zh_mapping() -> dict[str, dict[str, str]]:
    mapping: dict[str, dict[str, str]] = {}
    for path in ZH_DOCS_DIR.glob("*.md"):
        fm, _ = split_frontmatter(path.read_text(encoding="utf-8"))
        source_file = fm.get("source_file")
        if not source_file:
            continue
        mapping[source_file] = {
            "slug": path.stem,
            "source_code": fm.get("source_code", ""),
            "order_key": fm.get("order_key", ""),
        }
    return mapping


def fallback_slug(source_file: str) -> str:
    stem = source_file.removesuffix(".md")
    stem = re.sub(r"^03-行业评估-", "", stem)
    stem = stem.replace("_", "-")
    stem = re.sub(r"[^A-Za-z0-9-]+", "-", stem)
    stem = re.sub(r"-{2,}", "-", stem)
    return stem.strip("-").lower()


def main() -> None:
    EN_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    mapping = zh_mapping()
    written = 0

    for path in sorted(EN_SOURCE_DIR.glob("*-English.md")):
        source_file = path.name.replace("-English.md", ".md")
        zh_meta = mapping.get(source_file, {})
        slug = zh_meta.get("slug") or fallback_slug(source_file)
        source_code = zh_meta.get("source_code", "")
        order_key = zh_meta.get("order_key", "")

        fm, body = split_frontmatter(path.read_text(encoding="utf-8"))
        fm["layout"] = "en_doc"
        fm["lang"] = "en"
        fm["source_file"] = source_file
        if source_code:
            fm["source_code"] = source_code
        if order_key:
            fm["order_key"] = order_key

        out = EN_DOCS_DIR / f"{slug}.md"
        out.write_text(dump_frontmatter(fm) + body.strip() + "\n", encoding="utf-8")
        written += 1

    print(f"synced {written} English drafts")


if __name__ == "__main__":
    main()
