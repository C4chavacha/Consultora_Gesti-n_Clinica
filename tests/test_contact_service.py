import unittest
from unittest.mock import patch

from services.contact_service import contact_fingerprint, deliver_contact, validate_contact


VALID_CONTACT = {
    "nombre": "Ana Pérez",
    "institucion": "Hospital de prueba",
    "cargo": "Directora de operaciones",
    "correo": "ana@example.org",
    "telefono": "+56 9 1234 5678",
    "tipo_solicitud": "Conversación inicial",
    "interes": "Diagnóstico clínico-operacional",
    "desafio": "Necesitamos revisar la planificación de capacidad.",
    "acepta_contacto": True,
}


class ContactServiceTests(unittest.TestCase):
    def test_valid_contact_has_no_errors(self):
        self.assertEqual(validate_contact(VALID_CONTACT), {})

    def test_invalid_contact_reports_required_email_and_consent(self):
        invalid = {**VALID_CONTACT, "nombre": "", "correo": "correo-invalido", "acepta_contacto": False}
        errors = validate_contact(invalid)
        self.assertIn("nombre", errors)
        self.assertIn("correo", errors)
        self.assertIn("acepta_contacto", errors)

    def test_demo_mode_never_claims_delivery(self):
        result = deliver_contact(VALID_CONTACT, webhook_url="")
        self.assertTrue(result.ok)
        self.assertFalse(result.delivered)
        self.assertIn("no fue enviada", result.message)

    def test_duplicate_fingerprint_is_stable(self):
        reordered = dict(reversed(list(VALID_CONTACT.items())))
        self.assertEqual(contact_fingerprint(VALID_CONTACT), contact_fingerprint(reordered))

    @patch("services.contact_service.urlopen")
    def test_configured_webhook_confirms_delivery_only_on_success(self, mocked_urlopen):
        response = mocked_urlopen.return_value.__enter__.return_value
        response.status = 202
        result = deliver_contact(VALID_CONTACT, "https://example.org/contact")
        self.assertTrue(result.delivered)
        self.assertIn("correctamente", result.message)


if __name__ == "__main__":
    unittest.main()

