#!/usr/bin/env python3
# ABOUTME: Renders the sprint page (index.html) and each design's notes page from the
# ABOUTME: HTML templates in site/ plus the Markdown that the four sessions wrote.
import re
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DESIGNS_DIR = ROOT / "designs"

# Facts the placards show. Seed lengths come from each session's own notes;
# image counts are read from the synced assets folder.
DESIGNS = [
    {
        "slug": "01-shotgun-house",
        "num": "01",
        "name": "Shotgun house",
        "layer": "Structure",
        "line": "One long walk through five rooms. The Slack is the kitchen at the back.",
        "type": "Fraunces and Libre Franklin",
        "seed": "192 characters",
    },
    {
        "slug": "02-front-porch",
        "num": "02",
        "name": "Front porch",
        "layer": "Scene",
        "line": "A warm evening, a few people already there, and one empty chair.",
        "type": "Newsreader and Work Sans",
        "seed": "192 characters",
    },
    {
        "slug": "03-shop-sign",
        "num": "03",
        "name": "Shop sign",
        "layer": "Type",
        "line": "Hand-painted corner-store signage for the headlines, a quiet sans for the rest.",
        "type": "Painted lettering and Libre Franklin",
        "seed": "128 characters",
    },
    {
        "slug": "04-combined",
        "num": "04",
        "name": "Combined",
        "layer": "All three, one job each",
        "line": "The house is the sequence, the porch is the feeling, the signs are the voice.",
        "type": "Libre Franklin and Karla",
        "seed": "192 characters",
    },
]

MD = markdown.Markdown(extensions=["extra", "sane_lists"])


def render_md(path: Path) -> str:
    MD.reset()
    return MD.convert(path.read_text(encoding="utf-8"))


def fill(template: str, values: dict) -> str:
    out = template
    for key, value in values.items():
        out = out.replace("{{" + key + "}}", value)
    missing = re.findall(r"{{(\w+)}}", out)
    if missing:
        sys.exit(f"unfilled placeholders: {sorted(set(missing))}")
    return out


def image_count(slug: str) -> int:
    assets = DESIGNS_DIR / slug / "assets"
    return sum(1 for p in assets.iterdir() if p.suffix in {".webp", ".png", ".jpg"})


def shot(slug: str, label: str) -> str | None:
    path = SITE / "shots" / f"{slug}-{label}.webp"
    return f"site/shots/{path.name}" if path.is_file() else None


def full_page(slug: str, label: str) -> str | None:
    shots = DESIGNS_DIR / slug / "screenshots"
    if not shots.is_dir():
        return None
    for name in (f"{label}-full.webp", f"{label}-00-full-page.webp"):
        if (shots / name).is_file():
            return f"designs/{slug}/screenshots/{name}"
    return None


def is_done(slug: str) -> bool:
    return (DESIGNS_DIR / slug / "NOTES.md").is_file()


def build_exhibit(d: dict, template: str) -> str:
    slug = d["slug"]
    facts = [("Layer", d["layer"]), ("Type", d["type"]), ("Seed string", d["seed"])]
    facts.append(("Generated images", str(image_count(slug))))
    facts.append(("Status", "Built, not yet critiqued" if is_done(slug) else "Session still running"))
    facts_html = "\n".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)

    desktop = shot(slug, "desktop")
    mobile = shot(slug, "mobile")
    figure = (
        f'<a class="frame frame--desktop" href="designs/{slug}/">'
        f'<img src="{desktop}" alt="{d["name"]} homepage at desktop width" loading="lazy" width="1440" height="900"></a>'
        if desktop
        else '<div class="frame frame--desktop frame--empty"><p>No screenshot yet. The session is still working.</p></div>'
    )
    mobile_html = (
        f'<a class="frame frame--mobile" href="designs/{slug}/">'
        f'<img src="{mobile}" alt="{d["name"]} homepage at phone width" loading="lazy" width="780" height="1688"></a>'
        if mobile
        else ""
    )
    links = [f'<a class="button" href="designs/{slug}/">Open the design</a>']
    if (DESIGNS_DIR / slug / "DESIGN-NOTE.md").is_file():
        links.append(f'<a href="designs/{slug}/notes.html">Design note and build notes</a>')
    for label, name in (("desktop", "Full page, desktop"), ("mobile", "Full page, phone")):
        fp = full_page(slug, label)
        if fp:
            links.append(f'<a href="{fp}">{name}</a>')

    return fill(
        template,
        {
            "slug": slug,
            "num": d["num"],
            "name": d["name"],
            "line": d["line"],
            "facts": facts_html,
            "figure": figure,
            "mobile": mobile_html,
            "links": "\n".join(links),
            "prompt": render_md(DESIGNS_DIR / slug / "PROMPT.md"),
        },
    )


def build_wall() -> str:
    frames = []
    for d in DESIGNS:
        desktop = shot(d["slug"], "desktop")
        img = (
            f'<img src="{desktop}" alt="" width="1440" height="900">'
            if desktop
            else '<span class="wall-empty">Still building</span>'
        )
        frames.append(
            f'<a class="wall-frame" href="#{d["slug"]}">{img}'
            f'<span class="wall-label"><b>{d["num"]}</b> {d["name"]}</span></a>'
        )
    return "\n".join(frames)


def build_notes_page(d: dict, template: str) -> None:
    slug = d["slug"]
    note = DESIGNS_DIR / slug / "DESIGN-NOTE.md"
    notes = DESIGNS_DIR / slug / "NOTES.md"
    if not note.is_file():
        return
    body = render_md(note)
    if notes.is_file():
        body += "\n<hr>\n" + render_md(notes)
    else:
        body += '\n<hr>\n<p class="muted">NOTES.md not written yet. The session is still running.</p>'
    html = fill(template, {"num": d["num"], "name": d["name"], "slug": slug, "body": body})
    (DESIGNS_DIR / slug / "notes.html").write_text(html, encoding="utf-8")


def main() -> None:
    page_tpl = (SITE / "template.html").read_text(encoding="utf-8")
    exhibit_tpl = (SITE / "exhibit.html").read_text(encoding="utf-8")
    notes_tpl = (SITE / "notes.html").read_text(encoding="utf-8")

    brief = render_md(DESIGNS_DIR / "01-shotgun-house" / "CLAUDE.md")
    critic = render_md(DESIGNS_DIR / "01-shotgun-house" / "CRITIC.md")
    polish = render_md(ROOT / "source" / "prompt-pack" / "POLISH.md")
    exhibits = "\n".join(build_exhibit(d, exhibit_tpl) for d in DESIGNS)

    index = fill(
        page_tpl,
        {"wall": build_wall(), "brief": brief, "critic": critic, "polish": polish, "exhibits": exhibits},
    )
    (ROOT / "index.html").write_text(index, encoding="utf-8")
    for d in DESIGNS:
        build_notes_page(d, notes_tpl)
    print("built index.html and notes pages")


if __name__ == "__main__":
    main()
