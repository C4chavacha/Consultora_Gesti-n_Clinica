import { describe, expect, it } from "vitest";
import { validateContact } from "../lib/contact";

const validContact = {
  nombre: "Ana Pérez",
  institucion: "Hospital de prueba",
  cargo: "Directora",
  correo: "ana@example.org",
  telefono: "+56 9 1234 5678",
  tipo_solicitud: "Conversación inicial",
  interes: "Consultoría GRD",
  desafio: "Necesitamos comprender mejor nuestros flujos.",
  acepta_contacto: true
};

describe("validación del contacto", () => {
  it("acepta y normaliza un contacto válido", () => {
    const result = validateContact({ ...validContact, nombre: "  Ana Pérez  " });
    expect(result.ok).toBe(true);
    if (result.ok) expect(result.data.nombre).toBe("Ana Pérez");
  });

  it("rechaza campos obligatorios vacíos", () => {
    const result = validateContact({ ...validContact, desafio: "" });
    expect(result).toEqual({ ok: false, message: "Completa los campos obligatorios para continuar." });
  });

  it("rechaza correos inválidos y ausencia de consentimiento", () => {
    expect(validateContact({ ...validContact, correo: "correo-invalido" }).ok).toBe(false);
    expect(validateContact({ ...validContact, acepta_contacto: false }).ok).toBe(false);
  });
});
