export type ContactPayload = {
  nombre: string;
  institucion: string;
  cargo: string;
  correo: string;
  telefono: string;
  tipo_solicitud: string;
  interes: string;
  desafio: string;
  acepta_contacto: boolean;
};

const limits: Record<Exclude<keyof ContactPayload, "acepta_contacto">, number> = {
  nombre: 100,
  institucion: 140,
  cargo: 120,
  correo: 180,
  telefono: 40,
  tipo_solicitud: 60,
  interes: 160,
  desafio: 1600
};

export function validateContact(input: unknown): { ok: true; data: ContactPayload } | { ok: false; message: string } {
  if (!input || typeof input !== "object" || Array.isArray(input)) {
    return { ok: false, message: "La solicitud no tiene un formato válido." };
  }

  const source = input as Record<string, unknown>;
  const data = Object.fromEntries(
    Object.keys(limits).map((key) => [key, typeof source[key] === "string" ? source[key].trim() : ""])
  ) as Omit<ContactPayload, "acepta_contacto">;

  if (!data.nombre || !data.institucion || !data.correo || !data.interes || !data.desafio) {
    return { ok: false, message: "Completa los campos obligatorios para continuar." };
  }
  if (!source.acepta_contacto) {
    return { ok: false, message: "Necesitamos tu autorización para responder esta solicitud." };
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.correo)) {
    return { ok: false, message: "Ingresa un correo electrónico válido." };
  }
  for (const [key, limit] of Object.entries(limits)) {
    if (data[key as keyof typeof data].length > limit) {
      return { ok: false, message: "Uno de los campos supera el largo permitido." };
    }
  }

  return { ok: true, data: { ...data, acepta_contacto: true } };
}
