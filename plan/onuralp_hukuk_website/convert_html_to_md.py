#!/usr/bin/env python3
import html as html_lib
import os
import re
import shutil
from pathlib import Path

import html2text
from bs4 import BeautifulSoup, Comment

ROOT = Path(__file__).resolve().parent / "turhanhukukvedanismanlik.com.tr"
SOURCE_ROOT = Path("/Users/berkaydemiroren/Desktop/websites/onuralp_hukuk_copy/turhanhukukvedanismanlik.com.tr")
SITE_SUFFIX = re.compile(r"\s*[-|]\s*Avukat Onuralp.*", re.I)
JUNK_HTML_RE = re.compile(r"^index[0-9a-f]+\.html$", re.I)


def make_converter():
    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_images = True
    h.ignore_emphasis = False
    h.single_line_break = False
    h.unicode_snob = True
    h.skip_internal_links = False
    return h


def clean_text(text):
    if not text:
        return ""
    text = html_lib.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fix_links(md, html_path):
    def repl(match):
        label = match.group(1)
        href = match.group(2)
        if href.startswith(("http://", "https://", "mailto:", "tel:", "#")):
            return match.group(0)
        target = (html_path.parent / href).resolve()
        try:
            rel = os.path.relpath(target, html_path.parent)
        except ValueError:
            return match.group(0)
        rel = rel.replace("\\", "/")
        rel = re.sub(r"/index\.html$", "/", rel)
        rel = re.sub(r"\.html$", "", rel)
        if rel == ".":
            rel = "./"
        return f"[{label}]({rel})"

    return re.sub(r"\[([^\]]*)\]\(([^)]+)\)", repl, md)


def yaml_escape(value):
    if value is None:
        return '""'
    value = str(value).replace('"', '\\"')
    return f'"{value}"'


def extract_meta(soup):
    title_tag = soup.find("title")
    raw_title = clean_text(title_tag.get_text()) if title_tag else ""
    page_title = soup.select_one("h1.page-title")
    title = clean_text(page_title.get_text()) if page_title else SITE_SUFFIX.sub("", raw_title)

    desc_tag = soup.find("meta", attrs={"name": "description"})
    description = desc_tag.get("content", "").strip() if desc_tag else ""

    canonical = soup.find("link", attrs={"rel": "canonical"})
    og_url = soup.find("meta", attrs={"property": "og:url"})
    source = ""
    if og_url and og_url.get("content"):
        source = og_url["content"].strip()
    elif canonical and canonical.get("href"):
        source = canonical["href"].strip()

    published = soup.find("meta", attrs={"property": "article:published_time"})
    iso_date = published.get("content", "")[:10] if published else ""

    item_date = soup.select_one(".item-date")
    display_date = clean_text(item_date.get_text()) if item_date else ""

    category_el = soup.select_one(".entry-featured .item-category a") or soup.select_one(
        ".entry-meta .item-category a"
    )
    category = clean_text(category_el.get_text()) if category_el else ""

    return {
        "title": title,
        "description": description,
        "source": source,
        "iso_date": iso_date,
        "display_date": display_date,
        "category": category,
    }


def strip_boilerplate(content_el):
    for selector in ["#ez-toc-container", ".ez-toc-container", "script", "style"]:
        for node in content_el.select(selector):
            node.decompose()
    for comment in content_el.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()
    return content_el


def html_to_markdown(fragment_html, html_path):
    converter = make_converter()
    md = converter.handle(fragment_html)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    md = fix_links(md, html_path)
    return md


def build_frontmatter(meta, slug, page_type="page"):
    lines = ["---"]
    lines.append(f"title: {yaml_escape(meta['title'])}")
    if meta["description"]:
        lines.append(f"description: {yaml_escape(meta['description'])}")
    if meta["category"]:
        lines.append(f"category: {yaml_escape(meta['category'])}")
    if meta["iso_date"]:
        lines.append(f"date: {meta['iso_date']}")
    lines.append(f"slug: {slug}")
    lines.append(f"type: {page_type}")
    if meta["source"]:
        lines.append(f"source: {yaml_escape(meta['source'])}")
    lines.append("---")
    return "\n".join(lines)


def convert_content_page(html_path, soup):
    content_el = soup.select_one("div.entry-content.clearfix")
    if not content_el:
        return None

    meta = extract_meta(soup)
    rel_dir = html_path.parent.relative_to(ROOT)
    slug = rel_dir.name if rel_dir != Path(".") else "home"

    strip_boilerplate(content_el)
    body_md = html_to_markdown(str(content_el), html_path)

    parts = [build_frontmatter(meta, slug), "", f"# {meta['title']}", ""]
    if meta["category"] or meta["display_date"]:
        meta_bits = []
        if meta["category"]:
            meta_bits.append(f"**Kategori:** {meta['category']}")
        if meta["display_date"]:
            meta_bits.append(f"**Tarih:** {meta['display_date']}")
        parts.append("  \n".join(meta_bits))
        parts.append("")

    parts.append(body_md)
    return "\n".join(parts) + "\n"


def convert_archive_page(html_path, soup):
    meta = extract_meta(soup)
    rel_dir = html_path.parent.relative_to(ROOT)
    slug = "/".join(rel_dir.parts) if rel_dir != Path(".") else "home"

    articles = []
    for article in soup.select("article.single-hentry.archive"):
        title_el = article.select_one("h2.entry-title a")
        if not title_el:
            continue
        title = clean_text(title_el.get_text())
        href = title_el.get("href", "")
        date_el = article.select_one(".item-date")
        date = clean_text(date_el.get_text()) if date_el else ""
        excerpt_el = article.select_one(".entry-excerpt")
        excerpt = clean_text(excerpt_el.get_text()) if excerpt_el else ""
        excerpt = excerpt.replace("[…]", "…").replace("[&hellip;]", "…")
        articles.append({"title": title, "href": href, "date": date, "excerpt": excerpt})

    if not articles:
        return None

    parts = [build_frontmatter(meta, slug, "archive"), "", f"# {meta['title']}", "", "## Yazılar", ""]
    for item in articles:
        line = fix_links(f"- [{item['title']}]({item['href']})", html_path)
        if item["date"]:
            line += f" — {item['date']}"
        parts.append(line)
        if item["excerpt"]:
            parts.append(f"  {item['excerpt']}")
        parts.append("")

    return "\n".join(parts).strip() + "\n"


def output_path_for(html_path):
    if html_path.name == "index.html":
        return html_path.with_suffix(".md")
    return html_path.with_suffix(".md")


def is_junk_html(path):
    rel = path.relative_to(ROOT)
    parts = rel.parts
    if "revslider" in parts or "feed" in parts:
        return True
    if path.name == "${e1d2c.html":
        return True
    if "wp-content" in parts or "wp-json" in parts or "gmpg.org" in parts:
        return True
    if path.parent == ROOT and JUNK_HTML_RE.match(path.name):
        return True
    return False


def should_delete_duplicate_root_html(path):
    if path.parent != ROOT or path.suffix != ".html":
        return False
    if path.name == "index.html":
        return False
    stem = path.stem
    if (ROOT / stem / "index.html").exists() or (ROOT / stem / "index.md").exists():
        return True
    return False


def fix_from_source():
    fixed_content = 0
    fixed_archive = 0
    for md_path in sorted(ROOT.rglob("index.md")):
        rel = md_path.parent.relative_to(ROOT)
        source_html = SOURCE_ROOT / rel / "index.html"
        if not source_html.exists():
            continue
        soup = BeautifulSoup(source_html.read_text(encoding="utf-8", errors="replace"), "html.parser")
        fake_html = ROOT / rel / "index.html"
        if soup.select_one("div.entry-content.clearfix"):
            md_content = convert_content_page(fake_html, soup)
            kind = "content"
        elif soup.select("article.single-hentry.archive"):
            md_content = convert_archive_page(fake_html, soup)
            kind = "archive"
        else:
            continue
        if md_content:
            md_path.write_text(md_content, encoding="utf-8")
            if kind == "content":
                fixed_content += 1
            else:
                fixed_archive += 1
    print(f"fixed_content={fixed_content} fixed_archive={fixed_archive}")


def main():
    converted = 0
    archived = 0
    deleted = 0
    skipped = 0

    html_files = sorted(ROOT.rglob("*.html"))

    for html_path in html_files:
        if is_junk_html(html_path) or should_delete_duplicate_root_html(html_path):
            html_path.unlink(missing_ok=True)
            deleted += 1
            continue

        try:
            html = html_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            skipped += 1
            continue

        if "Sayfa bulunamadı" in html and "revslider" in str(html_path):
            html_path.unlink(missing_ok=True)
            deleted += 1
            continue

        soup = BeautifulSoup(html, "html.parser")
        md_path = output_path_for(html_path)

        if soup.select_one("div.entry-content.clearfix"):
            md_content = convert_content_page(html_path, soup)
            kind = "content"
        elif soup.select("article.single-hentry.archive"):
            md_content = convert_archive_page(html_path, soup)
            kind = "archive"
        else:
            html_path.unlink(missing_ok=True)
            deleted += 1
            continue

        if not md_content:
            html_path.unlink(missing_ok=True)
            deleted += 1
            continue

        md_path.write_text(md_content, encoding="utf-8")
        html_path.unlink(missing_ok=True)
        if kind == "content":
            converted += 1
        else:
            archived += 1

    for path in sorted(ROOT.rglob("*"), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()

    print(f"converted={converted} archive={archived} deleted_junk={deleted} skipped={skipped}")
    remaining_html = list(ROOT.rglob("*.html"))
    print(f"remaining_html={len(remaining_html)}")
    md_count = len(list(ROOT.rglob("*.md")))
    print(f"md_files={md_count}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--fix-from-source":
        fix_from_source()
    elif len(sys.argv) > 1 and sys.argv[1] == "--fix-archives":
        fix_from_source()
    else:
        main()
