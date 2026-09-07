"use client";

import { FormEvent, useState } from "react";
import { ArrowUpRight, LoaderCircle } from "lucide-react";
import { interestOptions } from "@/lib/content";

type FormState = "idle" | "sending" | "success" | "demo" | "error";

export function ContactForm() {
  const [state, setState] = useState<FormState>("idle");
  const [message, setMessage] = useState("");

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setState("sending");
    setMessage("");
    const form = event.currentTarget;
    const formData = new FormData(form);
    const payload = Object.fromEntries(formData.entries()) as Record<string, unknown>;
    payload.acepta_contacto = formData.get("acepta_contacto") === "on";
    const fingerprint = JSON.stringify(payload);

    if (sessionStorage.getItem("ultimo_contacto") === fingerprint) {
      setState("error");
      setMessage("Esta solicitud ya fue procesada durante tu sesión.");
      return;
    }

    try {
      const response = await fetch("/api/contact", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(payload)
      });
      const result = (await response.json()) as { ok?: boolean; delivered?: boolean; message?: string };
      setMessage(result.message ?? "No pudimos procesar la solicitud.");
      if (!response.ok || !result.ok) {
        setState("error");
        return;
      }
      sessionStorage.setItem("ultimo_contacto", fingerprint);
      setState(result.delivered ? "success" : "demo");
      if (result.delivered) form.reset();
    } catch {
      setState("error");
      setMessage("No fue posible conectar con el formulario. Revisa tu conexión e inténtalo nuevamente.");
    }
  }

  return (
    <form className="contact-form" onSubmit={submit} noValidate>
      <div className="form-heading"><span>CUÉNTANOS TU DESAFÍO</span><b>* obligatorio</b></div>
      <div className="form-grid">
        <label>Nombre y apellido *<input name="nombre" required maxLength={100} autoComplete="name" /></label>
        <label>Institución *<input name="institucion" required maxLength={140} autoComplete="organization" /></label>
        <label>Cargo<input name="cargo" maxLength={120} autoComplete="organization-title" /></label>
        <label>Correo corporativo *<input name="correo" type="email" required maxLength={180} autoComplete="email" /></label>
        <label>Teléfono<input name="telefono" type="tel" maxLength={40} autoComplete="tel" /></label>
        <label>Tipo de solicitud<select name="tipo_solicitud" defaultValue="Conversación inicial"><option>Conversación inicial</option><option>Proyecto o diagnóstico</option><option>Implementación de Equia</option><option>Alianza</option></select></label>
        <label className="form-wide">Área de interés *<select name="interes" required defaultValue=""><option value="" disabled>Selecciona una opción</option>{interestOptions.map((option) => <option key={option}>{option}</option>)}</select></label>
        <label className="form-wide">¿Qué desafío quieren resolver? *<textarea name="desafio" required maxLength={1600} rows={4} placeholder="Describe brevemente el contexto y el resultado que buscan." /></label>
      </div>
      <label className="consent"><input name="acepta_contacto" type="checkbox" required /> <span>Autorizo que me contacten para responder esta solicitud. No incluyas datos de pacientes ni información clínica sensible.</span></label>
      <button className="submit-button" type="submit" disabled={state === "sending"}>
        {state === "sending" ? <><LoaderCircle className="spin" size={18} /> Enviando…</> : <>Enviar solicitud <ArrowUpRight size={18} /></>}
      </button>
      {message && <p className={`form-message ${state}`} role="status">{message}</p>}
    </form>
  );
}
