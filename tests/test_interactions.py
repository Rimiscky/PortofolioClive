"""Contrôles de comportement dans un vrai navigateur Chromium."""
import contextlib
import functools
import http.server
import threading
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from playwright.sync_api import sync_playwright
from scripts.build import build_site


class InteractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = TemporaryDirectory()
        folder = Path(cls.tmp.name)
        build_site(folder)
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(folder))
        cls.server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f'http://127.0.0.1:{cls.server.server_port}'
        cls.pw = sync_playwright().start()
        cls.browser = cls.pw.chromium.launch()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close(); cls.pw.stop()
        cls.server.shutdown(); cls.server.server_close(); cls.tmp.cleanup()

    def test_navigation_remains_accessible_without_javascript(self):
        page = self.browser.new_page(viewport={'width': 375, 'height': 812}, java_script_enabled=False)
        page.goto(self.base + '/index.html')
        nav = page.get_by_role('navigation', name='Navigation principale')
        self.assertTrue(nav.is_visible())
        self.assertTrue(nav.get_by_role('link', name='Projets').is_visible())
        page.close()

    def test_all_filters_wrap_on_mobile(self):
        page = self.browser.new_page(viewport={'width': 375, 'height': 812})
        page.goto(self.base + '/projets.html')
        data = page.locator('.filters').evaluate('(el) => [el.scrollWidth, el.clientWidth]')
        self.assertLessEqual(data[0], data[1] + 1)
        page.close()

    def test_mobile_menu_opens_and_closes_with_escape(self):
        page = self.browser.new_page(viewport={'width': 375, 'height': 812})
        page.goto(self.base + '/index.html')
        menu = page.locator('.menu-toggle')
        self.assertEqual(menu.get_attribute('aria-label'), 'Ouvrir le menu')
        self.assertEqual(menu.get_attribute('aria-expanded'), 'false')
        menu.click()
        self.assertEqual(menu.get_attribute('aria-expanded'), 'true')
        self.assertTrue(page.get_by_role('navigation', name='Navigation principale').is_visible())
        page.keyboard.press('Escape')
        self.assertEqual(menu.get_attribute('aria-expanded'), 'false')
        page.close()

    def test_mobile_hero_image_starts_within_first_screen(self):
        page = self.browser.new_page(viewport={'width': 375, 'height': 812})
        page.goto(self.base + '/index.html')
        box = page.locator('.hero-photo').bounding_box()
        self.assertIsNotNone(box)
        self.assertLess(box['y'] if box else 9999, 650)
        page.close()

    def test_photo_hover_has_a_single_light_sweep_without_affecting_links(self):
        page = self.browser.new_page(viewport={'width': 1280, 'height': 800})
        page.goto(self.base + '/projets.html')
        card = page.locator('.project-link').first
        photo = card.locator('.project-image')
        before = photo.evaluate("el => getComputedStyle(el, '::after').transform")
        card.hover()
        page.wait_for_timeout(850)
        after = photo.evaluate("el => getComputedStyle(el, '::after').transform")
        self.assertNotEqual(before, after)
        self.assertTrue((card.get_attribute('href') or '').endswith('.html'))
        page.close()

    def test_hero_entrance_respects_reduced_motion(self):
        page = self.browser.new_page(viewport={'width': 375, 'height': 812})
        page.goto(self.base + '/index.html')
        self.assertNotEqual(page.locator('.hero-photo img').evaluate('el => getComputedStyle(el).animationName'), 'none')
        page.close()
        reduced = self.browser.new_page(viewport={'width': 375, 'height': 812}, reduced_motion='reduce')
        reduced.goto(self.base + '/index.html')
        duration = reduced.locator('.hero-photo img').evaluate('el => getComputedStyle(el).animationDuration')
        self.assertIn(duration, ('1e-05s', '0.00001s', '0.01ms', '0s'))
        reduced.close()

    def test_case_study_images_can_be_opened_full_size(self):
        page = self.browser.new_page(viewport={'width': 375, 'height': 812})
        page.goto(self.base + '/projets/les-delices-de-md.html')
        image = page.locator('.case-figure img').first
        self.assertTrue(image.locator('xpath=..').evaluate('(a) => a.tagName === "A" && a.href === a.firstElementChild.src'))
        page.close()

    def test_filter_reduces_cards_and_announces_count(self):
        page = self.browser.new_page(viewport={'width': 375, 'height': 812})
        page.goto(self.base + '/projets.html')
        page.get_by_role('button', name='Packaging').click()
        self.assertEqual(page.locator('.gallery-grid .project-card:visible').count(), 1)
        self.assertEqual(page.locator('.result-count').text_content(), '1 projet')
        page.get_by_role('button', name='Tous').click()
        self.assertEqual(page.locator('.gallery-grid .project-card:visible').count(), 11)
        page.close()


if __name__ == '__main__':
    unittest.main()
