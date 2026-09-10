export const site = {
  consultancyName: "[NOMBRE DE LA CONSULTORA]",
  eyebrow: "GESTIÓN CLÍNICA · OPERACIONES · TECNOLOGÍA",
  headline: "Experiencia clínica y tecnología para transformar la gestión en salud.",
  lead: "Ayudamos a organizaciones de salud a convertir desafíos operacionales en procesos mejor coordinados, decisiones informadas y soluciones aplicables."
};

export const views = [
  { key: "inicio", label: "Inicio" },
  { key: "enfoque", label: "Enfoque" },
  { key: "servicios", label: "Servicios" },
  { key: "equia", label: "Equia" },
  { key: "metodologia", label: "Método" },
  { key: "equipo", label: "Equipo" },
  { key: "preguntas", label: "Preguntas" },
  { key: "contacto", label: "Conversemos" }
] as const;

export type ViewKey = (typeof views)[number]["key"];

export function resolveView(value?: string | string[]): ViewKey {
  const candidate = Array.isArray(value) ? value[0] : value;
  return views.some(({ key }) => key === candidate) ? (candidate as ViewKey) : "inicio";
}

export const capabilities = [
  { number: "01", icon: "Stethoscope", title: "Visión clínica", body: "Soluciones conectadas con la realidad asistencial y la gestión médica." },
  { number: "02", icon: "Workflow", title: "Operación hospitalaria", body: "Diseño desde los flujos, restricciones y decisiones del trabajo diario." },
  { number: "03", icon: "ChartNoAxesCombined", title: "Analítica aplicada", body: "Indicadores y modelos que convierten información en una herramienta de gestión." },
  { number: "04", icon: "Cpu", title: "Tecnología útil", body: "Implementación de herramientas concretas, acompañadas por nuestro equipo." }
] as const;

export const services = [
  { icon: "SearchCheck", title: "Diagnóstico clínico-operacional", body: "Procesos, capacidad, flujos, indicadores y oportunidades de mejora." },
  { icon: "Shuffle", title: "Rediseño de procesos", body: "Soluciones aplicables para mejorar coordinación, continuidad y uso de recursos." },
  { icon: "UsersRound", title: "Dotación y capacidad", body: "Planificación de personas, jornadas, turnos, camas, pabellones y recursos críticos." },
  { icon: "Route", title: "Flujos asistenciales", body: "Mejora de urgencias, hospitalización, pabellón y coordinación entre unidades." },
  { icon: "ChartSpline", title: "Analítica y gestión", body: "Indicadores, modelos de datos y tableros para seguimiento ejecutivo y operacional." },
  { icon: "CircleDollarSign", title: "Consultoría GRD", body: "Evaluación clínico-financiera de escenarios, capacidad y sostenibilidad económica." },
  { icon: "Layers3", title: "Implementación de Equia", body: "Configuración de módulos según procesos, datos y necesidades institucionales." },
  { icon: "GraduationCap", title: "Capacitación y acompañamiento", body: "Formación de equipos, soporte a la adopción y mejora continua." }
] as const;

export const modules = [
  { code: "TU", name: "Turnos de Urgencias", body: "Planificación mensual de equipos, cobertura, ausencias, restricciones, equidad y ajustes operacionales.", tag: "Planificación", status: "Disponible" },
  { code: "BI", name: "Business Intelligence de Urgencias", body: "Indicadores, comparaciones, tendencias y proyecciones para comprender la actividad de urgencias.", tag: "Analítica", status: "Disponible" },
  { code: "TP", name: "Turnos de Pabellón", body: "Planificación de pabellones, Recuperación y Preanestesia, con jornadas, cobertura y colaciones.", tag: "Operaciones", status: "Disponible" },
  { code: "DP", name: "Destinos Postoperatorios", body: "Cruce de agenda y protocolos para identificar casos que deben revisarse o corregirse.", tag: "Flujo clínico", status: "Disponible" },
  { code: "GRD", name: "GRD Decision Engine", body: "Escenarios clínico-financieros, contratos, costos, capacidad, portafolios y Score Equia explicable.", tag: "Decisiones", status: "Disponible" },
  { code: "DF", name: "Dimensión financiera", body: "Ingresos, costos, contratos y escenarios para conectar decisiones clínicas con sostenibilidad financiera.", tag: "Gestión financiera", status: "En desarrollo" }
] as const;

export const methodology = [
  { number: "01", title: "Diagnóstico inicial", body: "Comprendemos el desafío, los actores, los datos y las restricciones." },
  { number: "02", title: "Definición y propuesta", body: "Priorizamos objetivos, alcance y una ruta de trabajo verificable." },
  { number: "03", title: "Diseño de solución", body: "Rediseñamos procesos o parametrizamos las herramientas necesarias." },
  { number: "04", title: "Piloto controlado", body: "Probamos en un alcance acotado, recogemos evidencia y ajustamos." },
  { number: "05", title: "Implementación", body: "Integramos la solución al trabajo real de los equipos." },
  { number: "06", title: "Capacitación", body: "Preparamos a usuarios y líderes para operar y sostener el cambio." },
  { number: "07", title: "Acompañamiento", body: "Seguimos resultados, aprendizajes y oportunidades de mejora continua." }
] as const;

export const methodologyPhases = [
  {
    number: "01",
    name: "Comprender",
    headline: "Mirar antes de actuar.",
    body: "Entendemos el contexto y acordamos dónde concentrar el esfuerzo.",
    steps: ["01", "02"]
  },
  {
    number: "02",
    name: "Transformar",
    headline: "Diseñar y probar.",
    body: "Convertimos la intención en una solución aplicable y verificable.",
    steps: ["03", "04", "05"]
  },
  {
    number: "03",
    name: "Sostener",
    headline: "Dejar capacidad instalada.",
    body: "Acompañamos a los equipos para que el cambio pueda mantenerse.",
    steps: ["06", "07"]
  }
] as const;

export const team = [
  { initials: "RH", name: "Rodrigo Hernández", role: "Socio fundador y Director Médico", bio: "Lidera la visión clínica y orienta soluciones alineadas con las necesidades asistenciales y la gestión médica.", photo: "/assets/team/rodrigo-hernandez.jpg" },
  { initials: "FM", name: "Felipe Muñoz", role: "Socio fundador y Director de Operaciones Clínicas", bio: "Conecta el análisis de procesos clínico-operacionales con su implementación en terreno.", photo: "/assets/team/felipe-munoz.jpg" },
  { initials: "SV", name: "Sofía Vergara", role: "Socia fundadora y Directora de Flujo Hospitalario", bio: "Lidera soluciones de capacidad, hospitalización, coordinación asistencial y continuidad del flujo.", photo: "/assets/team/sofia-vergara-edited.png" },
  { initials: "FC", name: "Fabián Cifuentes", role: "Socio fundador y Director Ejecutivo", bio: "Lidera la estrategia, el desarrollo de negocios y la evolución de Equia, integrando gestión, analítica y tecnología.", photo: "/assets/team/fabian-cifuentes.jpg" }
] as const;

export const faqs = [
  { question: "¿La consultoría se adapta a cada institución?", answer: "Sí. El alcance se define según el desafío, la información disponible, la madurez operacional y las prioridades de cada organización." },
  { question: "¿Es necesario implementar todos los módulos de Equia?", answer: "No. Cada institución puede comenzar por un módulo o un piloto acotado y ampliar el alcance cuando exista valor demostrado." },
  { question: "¿Equia reemplaza los sistemas clínicos existentes?", answer: "No. Equia está pensada como una capa de apoyo operacional y analítico, complementaria a los sistemas oficiales de la institución." },
  { question: "¿Se puede comenzar con un piloto?", answer: "Sí. Un piloto permite validar supuestos, datos, adopción y resultados antes de una implementación más amplia." },
  { question: "¿Qué información se necesita para iniciar?", answer: "Depende del desafío. La primera conversación identifica fuentes mínimas, responsables, restricciones y resguardos necesarios." },
  { question: "¿Cómo se protegen los datos utilizados?", answer: "El tratamiento de datos, accesos, infraestructura y responsabilidades se define formalmente antes de cada proyecto. No se solicitan datos clínicos sensibles mediante esta web." }
] as const;

export const interestOptions = [
  "Diagnóstico clínico-operacional",
  "Procesos y flujos asistenciales",
  "Planificación de dotación y capacidad",
  "Analítica e inteligencia de negocios",
  "Consultoría GRD",
  "Equia · Turnos de Urgencias",
  "Equia · Business Intelligence",
  "Equia · Turnos de Pabellón",
  "Equia · Destinos Postoperatorios",
  "Equia · GRD Decision Engine",
  "Equia · Dimensión financiera",
  "Otro / por definir"
] as const;
