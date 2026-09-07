import { NextResponse } from "next/server";
import { validateContact } from "@/lib/contact";

export const runtime = "nodejs";

export async function POST(request: Request) {
  if (!request.headers.get("content-type")?.includes("application/json")) {
    return NextResponse.json({ ok: false, message: "El formulario debe enviarse como JSON." }, { status: 415 });
  }

  let input: unknown;
  try {
    input = await request.json();
  } catch {
    return NextResponse.json({ ok: false, message: "No pudimos leer la solicitud." }, { status: 400 });
  }

  const validation = validateContact(input);
  if (!validation.ok) {
    return NextResponse.json(validation, { status: 400 });
  }

  const webhookUrl = process.env.CONTACT_WEBHOOK_URL?.trim();
  if (!webhookUrl) {
    return NextResponse.json({
      ok: true,
      delivered: false,
      message: "Datos validados en modo demostración. Aún no existe un canal de envío configurado."
    });
  }

  let webhook: URL;
  try {
    webhook = new URL(webhookUrl);
  } catch {
    return NextResponse.json({ ok: false, message: "El canal de contacto no está configurado correctamente." }, { status: 503 });
  }
  if (webhook.protocol !== "https:") {
    return NextResponse.json({ ok: false, message: "El canal de contacto requiere una conexión segura." }, { status: 503 });
  }

  try {
    const response = await fetch(webhook, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(validation.data),
      signal: AbortSignal.timeout(6000),
      cache: "no-store"
    });
    if (!response.ok) throw new Error("Webhook rejected the request");
  } catch {
    return NextResponse.json({ ok: false, message: "No pudimos entregar tu solicitud. Inténtalo nuevamente más tarde." }, { status: 502 });
  }

  return NextResponse.json({ ok: true, delivered: true, message: "Gracias. Recibimos tu solicitud y nos pondremos en contacto." });
}
