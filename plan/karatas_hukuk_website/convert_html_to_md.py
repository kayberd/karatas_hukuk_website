#!/usr/bin/env python3
import html as html_lib
import os
import re
from pathlib import Path

import html2text
from bs4 import BeautifulSoup, Comment

ROOT = Path(__file__).resolve().parent / "rusenkaratas.av.tr"
TITLE_SUFFIX = re.compile(r"\s*[-–|]\s*Av\.\s*M\.\s*Ruşen KARATAŞ.*", re.I)

CONTENT_DIRS = {
    "aile-hukuku",
    "ceza-hukuku",
    "is-hukuku",
    "idari-yargi",
    "yabancilar-hukuku",
    "tasinmaz-hukuku",
    "akademik-danismanlik",
    "hakkimizda",
    "contact-us",
    "pomem-saglik-raporu-sureci-nasil-isler",
    "blog",
}


def make_converter():
    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_images = True
    h.ignore_emphasis = False
    h.single_line_break = False
    h.unicode_snob = True
    return h


def clean_text(text):
    if not text:
        return ""
    return re.sub(r"\s+", " ", html_lib.unescape(text)).strip()


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
    value = str(value or "").replace('"', '\\"')
    return f'"{value}"'


def extract_meta(soup):
    title_tag = soup.find("title")
    raw_title = clean_text(title_tag.get_text()) if title_tag else ""
    h1 = soup.select_one(".guten-post-title h1")
    title = clean_text(h1.get_text()) if h1 else TITLE_SUFFIX.sub("", raw_title)

    desc_tag = soup.find("meta", attrs={"name": "description"})
    description = desc_tag.get("content", "").strip() if desc_tag else ""

    og_url = soup.find("meta", attrs={"property": "og:url"})
    canonical = soup.find("link", attrs={"rel": "canonical"})
    source = ""
    if og_url and og_url.get("content"):
        source = og_url["content"].strip()
    elif canonical and canonical.get("href"):
        source = canonical["href"].strip()

    published = soup.find("meta", attrs={"property": "article:published_time"})
    iso_date = published.get("content", "")[:10] if published else ""

    return {
        "title": title,
        "description": description,
        "source": source,
        "iso_date": iso_date,
    }


def strip_chrome(el):
    for selector in [
        "header",
        "footer",
        ".guten-nav-menu",
        "#firmly-header",
        ".guten-post-title",
        "script",
        "style",
        "noscript",
        "form",
        ".gutenverse-hamburger-wrapper",
    ]:
        for node in el.select(selector):
            node.decompose()
    for section in el.find_all("section"):
        if section.get("id") == "firmly-header":
            section.decompose()
    for comment in el.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()
    return el


FOOTER_MARKERS = (
    "Copyright ©",
    "Karataş Hukuk ve Danışmanlık; dürüstlük",
)


def clean_body(body):
    lines = body.splitlines()
    cut = len(lines)
    for i, line in enumerate(lines):
        if any(m in line for m in FOOTER_MARKERS):
            cut = i
            break
    lines = lines[:cut]
    out = []
    for line in lines:
        stripped = line.strip()
        if stripped in ("__", ""):
            if stripped == "":
                out.append("")
            continue
        if re.fullmatch(r"#{1,6}\s*", stripped):
            continue
        line = re.sub(r"\s*__\s*", " ", line).strip()
        line = re.sub(r"\[\s*\]\([^)]*\)", "", line).strip()
        if line:
            out.append(line)
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def build_frontmatter(meta, slug):
    lines = ["---", f"title: {yaml_escape(meta['title'])}"]
    if meta["description"]:
        lines.append(f"description: {yaml_escape(meta['description'])}")
    if meta["iso_date"]:
        lines.append(f"date: {meta['iso_date']}")
    lines.append(f"slug: {slug}")
    if meta["source"]:
        lines.append(f"source: {yaml_escape(meta['source'])}")
    lines.append("---")
    return "\n".join(lines)


def convert_page(html_path):
    html = html_path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(html, "html.parser")
    content_el = soup.select_one("div.entry-content.guten-post-content")
    if not content_el:
        return None
    meta = extract_meta(soup)
    rel_dir = html_path.parent.relative_to(ROOT)
    slug = rel_dir.name if rel_dir != Path(".") else "anasayfa"

    strip_chrome(content_el)
    converter = make_converter()
    body = converter.handle(str(content_el))
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    body = fix_links(body, html_path)
    body = clean_body(body)

    parts = [build_frontmatter(meta, slug), "", f"# {meta['title']}", "", body]
    return "\n".join(parts).strip() + "\n"


def main():
    converted = 0
    targets = []
    for d in CONTENT_DIRS:
        p = ROOT / d / "index.html"
        if p.exists():
            targets.append(p)
    home = ROOT / "index.html"
    if home.exists():
        targets.append(home)

    for html_path in targets:
        md = convert_page(html_path)
        if not md:
            continue
        (html_path.parent / "index.md").write_text(md, encoding="utf-8")
        converted += 1
        print(f"converted: {html_path.parent.relative_to(ROOT) or 'anasayfa'}")

    print(f"\ntotal converted={converted}")


if __name__ == "__main__":
    main()
