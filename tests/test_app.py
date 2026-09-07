import unittest
from pathlib import Path

from streamlit.testing.v1 import AppTest

from content import TEAM


class AppSmokeTests(unittest.TestCase):
    def test_home_renders_without_exception(self):
        app_path = Path(__file__).resolve().parents[1] / "app.py"
        app = AppTest.from_file(str(app_path), default_timeout=15).run()
        self.assertEqual(list(app.exception), [])
        rendered = "\n".join(element.value for element in app.markdown)
        self.assertIn("Experiencia clínica y tecnología", rendered)
        self.assertIn("Dimensión financiera", rendered)
        self.assertNotIn("Capa de Plata", rendered)
        self.assertIn("roadmap-canvas", rendered)
        self.assertIn("roadmap-road", rendered)
        self.assertEqual(rendered.count('class="roadmap-stop '), 7)
        self.assertEqual(rendered.count('class="capability-icon"'), 4)
        self.assertEqual(rendered.count('class="service-icon"'), 8)
        self.assertIn("Fabián Cifuentes", rendered)

    def test_configured_team_photos_exist(self):
        root = Path(__file__).resolve().parents[1]
        configured_photos = [photo for *_, photo in TEAM if photo]
        self.assertEqual(len(configured_photos), 3)
        for photo in configured_photos:
            self.assertTrue((root / photo).is_file(), photo)

    def test_roadmap_uses_compact_canvas(self):
        root = Path(__file__).resolve().parents[1]
        css = (root / "styles" / "site.css").read_text(encoding="utf-8")
        canvas_rule = css.split(".roadmap-canvas {", 1)[1].split("}", 1)[0]
        copy_rule = css.split(".roadmap-copy {", 1)[1].split("}", 1)[0]
        self.assertIn("min-height: 520px", canvas_rule)
        self.assertIn("border-radius: 26px", canvas_rule)
        self.assertIn("background: transparent", copy_rule)
        self.assertNotIn("backdrop-filter", copy_rule)


if __name__ == "__main__":
    unittest.main()
