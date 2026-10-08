import tempfile
import unittest
from pathlib import Path

from scripts.build import build_site


class PortfolioSiteTests(unittest.TestCase):
    def test_generated_pages_are_navigable_and_contain_real_projects(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            build_site(out)
            for page in ("index.html", "projets.html", "a-propos.html", "contact.html",
                         "projets/interim-industries.html", "projets/les-delices-de-md.html"):
                self.assertTrue((out / page).exists(), page)
            home = (out / "index.html").read_text(encoding="utf-8")
            self.assertIn("Clive Gouala", home)
            self.assertIn("projets.html", home)
            self.assertIn("Aller au contenu", home)
            listing = (out / "projets.html").read_text(encoding="utf-8")
            self.assertIn("Interim Industries", listing)
            self.assertIn("Les Délices de MD", listing)
            self.assertIn("Packaging", listing)

    def test_every_local_link_and_image_resolves_and_has_alt(self):
        from html.parser import HTMLParser
        class Links(HTMLParser):
            def __init__(self):
                super().__init__(); self.links = []; self.bad_images = []
            def handle_starttag(self, tag, attrs):
                a = dict(attrs)
                if tag in ('a','link') and (a.get('href') or '').startswith('/'):
                    self.links.append(a['href'])
                if tag in ('img','script') and (a.get('src') or '').startswith('/'):
                    self.links.append(a['src'])
                if tag == 'img' and not a.get('alt'):
                    self.bad_images.append(a.get('src'))
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp); build_site(out)
            for html in out.rglob('*.html'):
                p = Links(); p.feed(html.read_text(encoding='utf-8'))
                self.assertFalse(p.bad_images, f'{html}: {p.bad_images}')
                for link in p.links:
                    self.assertTrue((out / link.lstrip('/').split('#')[0]).exists(), f'{html}: {link}')


if __name__ == '__main__':
    unittest.main()
