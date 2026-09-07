import { describe, expect, it } from "vitest";
import { methodology, methodologyPhases, modules, resolveView, views } from "../lib/content";

describe("navegación pública", () => {
  it("conserva las ocho vistas y resuelve enlaces válidos", () => {
    expect(views).toHaveLength(8);
    expect(resolveView("equipo")).toBe("equipo");
    expect(resolveView(["contacto", "inicio"])).toBe("contacto");
  });

  it("vuelve a inicio frente a una vista desconocida", () => {
    expect(resolveView("no-existe")).toBe("inicio");
    expect(resolveView()).toBe("inicio");
  });

  it("presenta Equia como plataforma modular", () => {
    expect(modules).toHaveLength(6);
    expect(modules.map((module) => module.name)).toContain("Dimensión financiera");
  });

  it("agrupa las siete etapas en tres momentos sin perder ninguna", () => {
    expect(methodologyPhases.map((phase) => phase.name)).toEqual(["Comprender", "Transformar", "Sostener"]);
    const groupedSteps = methodologyPhases.flatMap((phase) => [...phase.steps]);
    expect(groupedSteps).toHaveLength(methodology.length);
    expect(new Set(groupedSteps).size).toBe(methodology.length);
  });
});
