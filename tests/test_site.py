# ABOUTME: Checks the built sprint site: local links resolve, every design ships an
# ABOUTME: index page and notes page, and no machine-local paths leak into HTML.
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DESIGNS = ["01-shotgun-house", "02-front-porch", "03-shop-sign", "04-combined"]
LINK_RE = re.compile(r'(?:href|src)="([^"#]+)(?:#[^"]*)?"')


def local_links(html_path: Path):
    text = html_path.read_text(encoding="utf-8")
    for target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "data:")):
            continue
        yield target


class BuiltSite(unittest.TestCase):
    def test_index_exists(self):
        self.assertTrue((ROOT / "index.html").is_file(), "run scripts/build.py")

    def test_every_design_has_pages(self):
        for name in DESIGNS:
            with self.subTest(design=name):
                self.assertTrue((ROOT / "designs" / name / "index.html").is_file())
                self.assertTrue((ROOT / "designs" / name / "notes.html").is_file())

    def test_local_links_resolve(self):
        pages = [ROOT / "index.html"] + [ROOT / "designs" / n / "notes.html" for n in DESIGNS]
        for page in pages:
            if not page.is_file():
                continue
            for target in local_links(page):
                with self.subTest(page=page.relative_to(ROOT), link=target):
                    resolved = (page.parent / target).resolve()
                    if target.endswith("/"):
                        resolved = resolved / "index.html"
                    self.assertTrue(resolved.exists(), f"{target} missing")

    def test_no_machine_paths(self):
        for page in ROOT.glob("**/*.html"):
            if "node_modules" in page.parts:
                continue
            text = page.read_text(encoding="utf-8", errors="ignore")
            with self.subTest(page=page.relative_to(ROOT)):
                self.assertNotIn("/Users/", text)
                self.assertNotIn("file://", text)


if __name__ == "__main__":
    unittest.main()
