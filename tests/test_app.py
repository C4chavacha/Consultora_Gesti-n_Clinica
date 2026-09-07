import unittest
from pathlib import Path

from streamlit.testing.v1 import AppTest

from content import TEAM


class AppSmokeTests(unittest.TestCase):
    @staticmethod
    def render_view(view: str | None = None):
        app_path = Path(__file__).resolve().parents[1] / "app.py"
        app = AppTest.from_file(str(app_path), default_timeout=15)
        if view is not None:
            app.query_params["vista"] = view
        app.run()
        rendered = "\n".join(element.value for element in app.markdown)
        return app, rendered

    def test_home_renders_without_exception(self):
        app, rendered = self.render_view()
        self.assertEqual(list(app.exception), [])
        self.assertIn("Experiencia clínica y tecnología", rendered)
        self.assertIn('data-view="inicio"', rendered)
        self.assertIn('href="?vista=enfoque"', rendered)
        self.assertNotIn('class="service-card"', rendered)
        self.assertNotIn('class="team-card"', rendered)

    def test_each_public_view_has_one_focused_surface(self):
        expectations = {
            "enfoque": ('class="capability-card"', 4),
            "servicios": ('class="service-card"', 8),
            "equia": ('class="module-card ', 6),
            "metodologia": ('class="roadmap-stop ', 7),
            "equipo": ('class="team-card"', 4),
        }
        for view, (selector, count) in expectations.items():
            with self.subTest(view=view):
                app, rendered = self.render_view(view)
                self.assertEqual(list(app.exception), [])
                self.assertIn(f'data-view="{view}"', rendered)
                self.assertEqual(rendered.count(selector), count)

        faq_app, faq_rendered = self.render_view("preguntas")
        self.assertEqual(list(faq_app.exception), [])
        self.assertIn('data-view="preguntas"', faq_rendered)
        self.assertEqual(len(faq_app.expander), 6)

        contact_app, contact_rendered = self.render_view("contacto")
        self.assertEqual(list(contact_app.exception), [])
        self.assertIn('data-view="contacto"', contact_rendered)
        self.assertEqual(len(contact_app.text_input), 5)
        self.assertEqual(len(contact_app.text_area), 1)

    def test_unknown_view_falls_back_to_home(self):
        app, rendered = self.render_view("vista-inexistente")
        self.assertEqual(list(app.exception), [])
        self.assertIn('data-view="inicio"', rendered)

    def test_equia_view_preserves_financial_module_name(self):
        _, rendered = self.render_view("equia")
        self.assertIn("Dimensión financiera", rendered)
        self.assertNotIn("Capa de Plata", rendered)

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
