"""Contenido editable del sitio comercial."""

SITE = {
    "consultancy_name": "[NOMBRE DE LA CONSULTORA]",
    "eyebrow": "GESTIÓN CLÍNICA · OPERACIONES · TECNOLOGÍA",
    "headline": "Experiencia clínica y tecnología para transformar la gestión en salud.",
    "lead": (
        "Ayudamos a organizaciones de salud a convertir desafíos operacionales en "
        "procesos mejor coordinados, decisiones informadas y soluciones aplicables."
    ),
}

CAPABILITIES = [
    ("01", "clinical", "Visión clínica", "Soluciones conectadas con la realidad asistencial y la gestión médica."),
    ("02", "operations", "Operación hospitalaria", "Diseño desde los flujos, restricciones y decisiones del trabajo diario."),
    ("03", "analytics", "Analítica aplicada", "Indicadores y modelos que convierten información en una herramienta de gestión."),
    ("04", "technology", "Tecnología útil", "Implementación de herramientas concretas, acompañadas por nuestro equipo."),
]

SERVICES = [
    ("diagnostic", "Diagnóstico clínico-operacional", "Procesos, capacidad, flujos, indicadores y oportunidades de mejora."),
    ("process", "Rediseño de procesos", "Soluciones aplicables para mejorar coordinación, continuidad y uso de recursos."),
    ("capacity", "Dotación y capacidad", "Planificación de personas, jornadas, turnos, camas, pabellones y recursos críticos."),
    ("flow", "Flujos asistenciales", "Mejora de urgencias, hospitalización, pabellón y coordinación entre unidades."),
    ("analytics", "Analítica y gestión", "Indicadores, modelos de datos y tableros para seguimiento ejecutivo y operacional."),
    ("finance", "Consultoría GRD", "Evaluación clínico-financiera de escenarios, capacidad y sostenibilidad económica."),
    ("platform", "Implementación de Equia", "Configuración de módulos según procesos, datos y necesidades institucionales."),
    ("training", "Capacitación y acompañamiento", "Formación de equipos, soporte a la adopción y mejora continua."),
]

MODULES = [
    {
        "code": "TU",
        "name": "Turnos de Urgencias",
        "body": "Planificación mensual de equipos, cobertura, ausencias, restricciones, equidad y ajustes operacionales.",
        "tag": "Planificación",
        "status": "Disponible",
    },
    {
        "code": "BI",
        "name": "Business Intelligence de Urgencias",
        "body": "Indicadores, comparaciones, tendencias y proyecciones para comprender la actividad de urgencias.",
        "tag": "Analítica",
        "status": "Disponible",
    },
    {
        "code": "TP",
        "name": "Turnos de Pabellón",
        "body": "Planificación de pabellones, Recuperación y Preanestesia, con jornadas, cobertura y colaciones.",
        "tag": "Operaciones",
        "status": "Disponible",
    },
    {
        "code": "DP",
        "name": "Destinos Postoperatorios",
        "body": "Cruce de agenda y protocolos para identificar casos que deben revisarse o corregirse.",
        "tag": "Flujo clínico",
        "status": "Disponible",
    },
    {
        "code": "GRD",
        "name": "GRD Decision Engine",
        "body": "Escenarios clínico-financieros, contratos, costos, capacidad, portafolios y Score Equia explicable.",
        "tag": "Decisiones",
        "status": "Disponible",
    },
    {
        "code": "DF",
        "name": "Dimensión financiera",
        "body": "Ingresos, costos, contratos y escenarios para conectar decisiones clínicas con sostenibilidad financiera.",
        "tag": "Gestión financiera",
        "status": "En desarrollo",
    },
]

METHODOLOGY = [
    ("01", "Diagnóstico inicial", "Comprendemos el desafío, los actores, los datos y las restricciones."),
    ("02", "Definición y propuesta", "Priorizamos objetivos, alcance y una ruta de trabajo verificable."),
    ("03", "Diseño de solución", "Rediseñamos procesos o parametrizamos las herramientas necesarias."),
    ("04", "Piloto controlado", "Probamos en un alcance acotado, recogemos evidencia y ajustamos."),
    ("05", "Implementación", "Integramos la solución al trabajo real de los equipos."),
    ("06", "Capacitación", "Preparamos a usuarios y líderes para operar y sostener el cambio."),
    ("07", "Acompañamiento", "Seguimos resultados, aprendizajes y oportunidades de mejora continua."),
]

TEAM = [
    ("RH", "Rodrigo Hernández", "Socio fundador y Director Médico", "Lidera la visión clínica y orienta soluciones alineadas con las necesidades asistenciales y la gestión médica.", "assets/team/rodrigo-hernandez.jpg"),
    ("FM", "Felipe Muñoz", "Socio fundador y Director de Operaciones Clínicas", "Conecta el análisis de procesos clínico-operacionales con su implementación en terreno.", "assets/team/felipe-munoz.jpg"),
    ("SV", "Sofía Vergara", "Socia fundadora y Directora de Flujo Hospitalario", "Lidera soluciones de capacidad, hospitalización, coordinación asistencial y continuidad del flujo.", None),
    ("FC", "Fabián Cifuentes", "Socio fundador y Director Ejecutivo", "Lidera la estrategia, el desarrollo de negocios y la evolución de Equia, integrando gestión, analítica y tecnología.", "assets/team/fabian-cifuentes.jpg"),
]

FAQS = [
    ("¿La consultoría se adapta a cada institución?", "Sí. El alcance se define según el desafío, la información disponible, la madurez operacional y las prioridades de cada organización."),
    ("¿Es necesario implementar todos los módulos de Equia?", "No. Cada institución puede comenzar por un módulo o un piloto acotado y ampliar el alcance cuando exista valor demostrado."),
    ("¿Equia reemplaza los sistemas clínicos existentes?", "No. Equia está pensada como una capa de apoyo operacional y analítico, complementaria a los sistemas oficiales de la institución."),
    ("¿Se puede comenzar con un piloto?", "Sí. Un piloto permite validar supuestos, datos, adopción y resultados antes de una implementación más amplia."),
    ("¿Qué información se necesita para iniciar?", "Depende del desafío. La primera conversación identifica fuentes mínimas, responsables, restricciones y resguardos necesarios."),
    ("¿Cómo se protegen los datos utilizados?", "El tratamiento de datos, accesos, infraestructura y responsabilidades se define formalmente antes de cada proyecto. No se solicitan datos clínicos sensibles mediante esta web."),
]

INTEREST_OPTIONS = [
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
    "Otro / por definir",
]
