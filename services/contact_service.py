"""Validación y entrega desacoplada de solicitudes comerciales."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import re
from typing import Mapping
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


EMAIL_PATTERN = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
REQUIRED_FIELDS = ("nombre", "institucion", "cargo", "correo", "tipo_solicitud", "interes", "desafio")
LIMITS = {
    "nombre": 100,
    "institucion": 140,
    "cargo": 120,
    "correo": 180,
    "telefono": 40,
    "tipo_solicitud": 80,
    "interes": 160,
    "desafio": 1200,
}


@dataclass(frozen=True)
class ContactResult:
    ok: bool
    delivered: bool
    message: str


def normalize_contact(data: Mapping[str, object]) -> dict[str, object]:
    normalized: dict[str, object] = {}
    for key, value in data.items():
        normalized[key] = value.strip() if isinstance(value, str) else value
    return normalized


def validate_contact(data: Mapping[str, object]) -> dict[str, str]:
    normalized = normalize_contact(data)
    errors: dict[str, str] = {}
    for field in REQUIRED_FIELDS:
        if not str(normalized.get(field, "")).strip():
            errors[field] = "Este campo es obligatorio."
    correo = str(normalized.get("correo", ""))
    if correo and not EMAIL_PATTERN.fullmatch(correo):
        errors["correo"] = "Ingresa un correo válido."
    for field, limit in LIMITS.items():
        if len(str(normalized.get(field, ""))) > limit:
            errors[field] = f"Máximo {limit} caracteres."
    if normalized.get("acepta_contacto") is not True:
        errors["acepta_contacto"] = "Debes aceptar ser contactado para enviar la solicitud."
    return errors


def contact_fingerprint(data: Mapping[str, object]) -> str:
    normalized = normalize_contact(data)
    stable = json.dumps(normalized, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(stable.encode("utf-8")).hexdigest()


def deliver_contact(data: Mapping[str, object], webhook_url: str | None, timeout: float = 6.0) -> ContactResult:
    errors = validate_contact(data)
    if errors:
        return ContactResult(False, False, "Revisa los campos indicados antes de continuar.")
    if not webhook_url:
        return ContactResult(
            True,
            False,
            "Formulario validado en modo demostración. La solicitud no fue enviada porque aún no existe un canal configurado.",
        )

    payload = json.dumps(normalize_contact(data), ensure_ascii=False).encode("utf-8")
    request = Request(
        webhook_url,
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "consultora-equia-web/1.0"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            if 200 <= response.status < 300:
                return ContactResult(True, True, "Solicitud enviada correctamente. Te contactaremos a la brevedad.")
            return ContactResult(False, False, "El canal de contacto no confirmó la recepción. Intenta nuevamente más tarde.")
    except (HTTPError, URLError, TimeoutError, ValueError):
        return ContactResult(False, False, "No fue posible entregar la solicitud. Intenta nuevamente o utiliza el correo de contacto.")
