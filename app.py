import base64
import mimetypes
import os
from pathlib import Path

import streamlit as st

from content import CAPABILITIES, FAQS, INTEREST_OPTIONS, METHODOLOGY, MODULES, SERVICES, SITE, TEAM
from services.contact_service import contact_fingerprint, deliver_contact, validate_contact


ROOT = Path(__file__).resolve().parent

ICON_PATHS = {
    "clinical": '<path d="M3 12h4l2.5-7 5 14 2.5-7H21"/>',
    "operations": '<rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/><path d="M10 6.5h5a2 2 0 0 1 2 2V14M14 17.5H9a2 2 0 0 1-2-2V10"/>',
    "analytics": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "technology": '<rect x="4" y="4" width="16" height="16" rx="3"/><path d="M9 9h6v6H9zM9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M20 9h3M1 15h3M20 15h3"/>',
    "diagnostic": '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5M8 10.5h5M10.5 8v5"/>',
    "process": '<path d="M4 7h11M12 4l3 3-3 3M20 17H9M12 14l-3 3 3 3"/>',
    "capacity": '<circle cx="9" cy="8" r="3"/><circle cx="17" cy="10" r="2.5"/><path d="M3 20c0-4 2.5-6 6-6s6 2 6 6M15 15c3.4 0 5 1.7 5 5"/>',
    "flow": '<circle cx="5" cy="6" r="2"/><circle cx="19" cy="18" r="2"/><path d="M7 6h5a4 4 0 0 1 4 4v1M17 8l-1 3-3-1M17 18h-5a4 4 0 0 1-4-4v-1M7 16l1-3 3 1"/>',
    "finance": '<circle cx="12" cy="12" r="9"/><path d="M15 8.5c-.7-.8-1.7-1.2-3-1.2-1.7 0-3 .9-3 2.3 0 3.5 6 1.6 6 5 0 1.4-1.3 2.4-3.1 2.4-1.4 0-2.6-.5-3.4-1.4M12 5v14"/>',
    "platform": '<path d="m12 3 9 5-9 5-9-5 9-5Z"/><path d="m3 12 9 5 9-5M3 16l9 5 9-5"/>',
    "training": '<path d="m3 9 9-5 9 5-9 5-9-5Z"/><path d="M7 12v5c3 2 7 2 10 0v-5M21 9v6"/>',
}

st.set_page_config(
    page_title=f"{SITE['consultancy_name']} | Gestión clínica e innovación",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def load_css() -> None:
    css = (ROOT / "styles" / "site.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def get_config_value(name: str, default: str = "") -> str:
    """Lee primero variables de entorno y luego secretos de Streamlit."""
    environment_value = os.getenv(name)
    if environment_value is not None:
        return environment_value
    try:
        return str(st.secrets.get(name, default))
    except Exception:
        return default


def icon_svg(name: str) -> str:
    """Renderiza iconografía lineal consistente y decorativa."""
    return (
        '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" '
        'fill="none" stroke="currentColor" stroke-width="1.7" '
        f'stroke-linecap="round" stroke-linejoin="round">{ICON_PATHS[name]}</svg>'
    )


def asset_data_uri(relative_path: str) -> str:
    """Convierte un recurso local optimizado en una URI embebida para el HTML."""
    asset_path = ROOT / relative_path
    mime_type = mimetypes.guess_type(asset_path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(asset_path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def render_portrait(initials: str, name: str, photo: str | None) -> str:
    if photo:
        return (
            '<div class="portrait-photo">'
            f'<img src="{asset_data_uri(photo)}" alt="Retrato de {name}" loading="lazy">'
            "</div>"
        )
    return (
        f'<div class="portrait-placeholder" aria-label="Fotografía pendiente de {name}">'
        f"<span>{initials}</span><small>FOTOGRAFÍA<br>PRÓXIMAMENTE</small></div>"
    )


def render_cards(items: list[tuple[str, str, str]], css_class: str) -> None:
    cards = "".join(
        f'<article class="{css_class}">'
        f'<div class="service-top"><span class="service-icon">{icon_svg(icon)}</span><b>{index:02}</b></div>'
        f'<h3>{title}</h3><p>{body}</p></article>'
        for index, (icon, title, body) in enumerate(items, start=1)
    )
    st.markdown(f'<div class="card-grid">{cards}</div>', unsafe_allow_html=True)


load_css()

st.markdown(
    f"""
    <header class="site-nav" aria-label="Navegación principal">
      <a class="wordmark" href="#inicio"><span class="wordmark-dot"></span>{SITE['consultancy_name']}</a>
      <nav>
        <a href="#servicios">Servicios</a>
        <a href="#equia">Equia</a>
        <a href="#metodologia">Metodología</a>
        <a href="#equipo">Equipo</a>
        <a class="nav-cta" href="#contacto">Conversemos</a>
      </nav>
    </header>
    """,
    unsafe_allow_html=True,
)

hero_text, hero_visual = st.columns([1.15, 0.85], gap="large", vertical_alignment="center")
with hero_text:
    st.markdown(
        f"""
        <section id="inicio" class="hero-copy">
          <div class="eyebrow"><span></span>{SITE['eyebrow']}</div>
          <h1>{SITE['headline']}</h1>
          <p>{SITE['lead']}</p>
          <div class="hero-actions">
            <a class="button primary" href="#contacto">Agenda una conversación <span>↗</span></a>
            <a class="button secondary" href="#equia">Conoce Equia <span>→</span></a>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

with hero_visual:
    st.markdown(
        """
        <div class="flow-panel" role="img" aria-label="Flujo conectado entre estrategia, operación y resultados">
          <div class="flow-topline"><span>TRANSFORMACIÓN APLICADA</span><b>● EN TERRENO</b></div>
          <div class="flow-core">
            <div class="flow-node node-a"><small>01</small><strong>Diagnóstico</strong><span>Comprender</span></div>
            <div class="flow-link"><i></i><i></i><i></i></div>
            <div class="flow-node node-b"><small>02</small><strong>Diseño</strong><span>Priorizar</span></div>
            <div class="flow-link"><i></i><i></i><i></i></div>
            <div class="flow-node node-c"><small>03</small><strong>Implementación</strong><span>Transformar</span></div>
          </div>
          <div class="flow-footer"><span>CLÍNICA</span><span>OPERACIONES</span><span>DATOS</span><span>TECNOLOGÍA</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="trust-line"><span>Del diagnóstico a la adopción</span><b></b><span>Diseño junto a los equipos</span><b></b><span>Decisiones trazables</span></div>', unsafe_allow_html=True)

st.markdown(
    """
    <section class="section intro-section">
      <span class="section-kicker">QUÉ NOS HACE DIFERENTES</span>
      <div class="section-heading split"><h2>Conocemos la complejidad<br>desde dentro.</h2><p>No entregamos solamente informes o software aislado. Conectamos estrategia, operación y tecnología para acompañar cambios que puedan sostenerse en la práctica.</p></div>
    </section>
    """,
    unsafe_allow_html=True,
)

capability_html = "".join(
    f'<article class="capability-card">'
    f'<div class="capability-top"><span class="capability-icon">{icon_svg(icon)}</span><b>{number}</b></div>'
    f'<h3>{title}</h3><p>{body}</p></article>'
    for number, icon, title, body in CAPABILITIES
)
st.markdown(f'<div class="capability-grid">{capability_html}</div>', unsafe_allow_html=True)

st.markdown(
    """
    <section id="servicios" class="section">
      <span class="section-kicker">SERVICIOS</span>
      <div class="section-heading"><h2>Capacidades para transformar<br>la gestión en salud.</h2><p>Partimos por el desafío real de cada institución y construimos una ruta de trabajo proporcional a su contexto y madurez operacional.</p></div>
    </section>
    """,
    unsafe_allow_html=True,
)
render_cards(SERVICES, "service-card")

equia_text, equia_logo = st.columns([1.3, 0.7], gap="large", vertical_alignment="center")
with equia_text:
    st.markdown(
        """
        <section id="equia" class="equia-copy">
          <span class="section-kicker light">PLATAFORMA TECNOLÓGICA</span>
          <h2>Equia convierte la estrategia operacional en herramientas concretas.</h2>
          <p>Un ecosistema clínico modular que reúne planificación, gestión operacional, analítica y apoyo a la toma de decisiones.</p>
          <a class="button light-button" href="#modulos">Explorar sus módulos <span>↓</span></a>
        </section>
        """,
        unsafe_allow_html=True,
    )
with equia_logo:
    st.image(str(ROOT / "assets" / "equia-mark.png"), width="stretch")

st.markdown('<div class="preview-spacer"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <section id="modulos" class="section module-section">
      <span class="section-kicker">MÓDULOS DE EQUIA</span>
      <div class="section-heading"><h2>Una plataforma.<br>Múltiples desafíos.</h2><p>Los módulos pueden implementarse de manera independiente y evolucionar junto con las necesidades de cada institución.</p></div>
    </section>
    """,
    unsafe_allow_html=True,
)
module_html = "".join(
    f'<article class="module-card {"roadmap" if module["status"] == "En desarrollo" else ""}">'
    f'<div class="module-head"><span>{module["code"]}</span><b>{module["status"]}</b></div>'
    f'<small>{module["tag"]}</small><h3>{module["name"]}</h3><p>{module["body"]}</p>'
    '</article>'
    for module in MODULES
)
st.markdown(f'<div class="module-grid">{module_html}</div>', unsafe_allow_html=True)
st.markdown(
    '<p class="product-note">Equia es una herramienta de apoyo a la gestión y a la toma de decisiones. No reemplaza el criterio clínico ni los sistemas oficiales de cada institución.</p>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section id="metodologia" class="section method-section">
      <span class="section-kicker">METODOLOGÍA</span>
      <div class="section-heading split"><h2>Una ruta clara,<br>adaptada a cada realidad.</h2><p>Cada proyecto se ajusta a la información disponible, la madurez operacional y las condiciones de implementación de la institución.</p></div>
    </section>
    """,
    unsafe_allow_html=True,
)
method_html = "".join(
    f'<li class="roadmap-stop {"row-top" if index <= 4 else "row-bottom"}">'
    f'<span class="roadmap-node"><b>{number}</b></span>'
    f'<div class="roadmap-copy"><small>ETAPA {number}</small><h3>{title}</h3><p>{body}</p></div>'
    '</li>'
    for index, (number, title, body) in enumerate(METHODOLOGY, start=1)
)
roadmap_svg = """
<svg class="roadmap-road" viewBox="0 0 1100 520" preserveAspectRatio="none" aria-hidden="true" focusable="false">
  <path class="road-edge" d="M70 165 H925 C1030 165 1030 355 925 355 H82" />
  <path class="road-surface" d="M70 165 H925 C1030 165 1030 355 925 355 H82" />
  <path class="road-centre" d="M70 165 H925 C1030 165 1030 355 925 355 H82" />
  <polygon class="road-arrow" points="28,355 84,323 84,387" />
</svg>
"""
st.markdown(
    f'<div class="roadmap-canvas">{roadmap_svg}<ol class="roadmap-stops" aria-label="Hoja de ruta de trabajo">{method_html}</ol></div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section id="equipo" class="section team-section">
      <span class="section-kicker">EQUIPO FUNDADOR</span>
      <div class="section-heading"><h2>Experiencia que conecta<br>lo clínico y lo operacional.</h2><p>Un equipo orientado a transformar conocimiento hospitalario en decisiones, procesos y herramientas aplicables.</p></div>
    </section>
    """,
    unsafe_allow_html=True,
)
team_html = "".join(
    f'<article class="team-card">'
    f'{render_portrait(initials, name, photo)}'
    f'<div class="team-content"><h3>{name}</h3><b>{role}</b><p>{bio}</p></div>'
    '</article>'
    for initials, name, role, bio, photo in TEAM
)
st.markdown(f'<div class="team-grid">{team_html}</div>', unsafe_allow_html=True)

st.markdown(
    """
    <section id="preguntas" class="section faq-section">
      <span class="section-kicker">PREGUNTAS FRECUENTES</span>
      <div class="section-heading"><h2>Comencemos por<br>lo esencial.</h2><p>La primera conversación permite definir si conviene una consultoría, un piloto o la implementación de un módulo de Equia.</p></div>
    </section>
    """,
    unsafe_allow_html=True,
)
for question, answer in FAQS:
    with st.expander(question):
        st.write(answer)

contact_intro, contact_form = st.columns([0.78, 1.22], gap="large", vertical_alignment="top")
with contact_intro:
    st.markdown(
        """
        <section id="contacto" class="contact-copy">
          <span class="section-kicker light">CONVERSEMOS</span>
          <h2>Todo cambio comienza por comprender bien el desafío.</h2>
          <p>Cuéntanos brevemente qué necesita tu institución. Podemos explorar una conversación inicial, un piloto o una demostración de Equia.</p>
          <div class="contact-detail"><small>CORREO</small><strong>[CORREO CORPORATIVO]</strong></div>
          <div class="contact-detail"><small>TELÉFONO</small><strong>[TELÉFONO]</strong></div>
          <p class="sensitive-note">No ingreses nombres de pacientes, diagnósticos ni otra información clínica sensible.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )

with contact_form:
    st.markdown('<div class="form-title"><span>SOLICITUD COMERCIAL</span><b>Campos con * son obligatorios</b></div>', unsafe_allow_html=True)
    with st.form("contact_form", clear_on_submit=False):
        first_row = st.columns(2)
        nombre = first_row[0].text_input("Nombre *", max_chars=100, placeholder="Tu nombre")
        institucion = first_row[1].text_input("Institución *", max_chars=140, placeholder="Clínica, hospital u organización")
        second_row = st.columns(2)
        cargo = second_row[0].text_input("Cargo *", max_chars=120, placeholder="Tu función")
        correo = second_row[1].text_input("Correo *", max_chars=180, placeholder="nombre@institucion.cl")
        third_row = st.columns(2)
        telefono = third_row[0].text_input("Teléfono", max_chars=40, placeholder="Opcional")
        tipo_solicitud = third_row[1].selectbox(
            "Tipo de solicitud *",
            ["Conversación inicial", "Demostración de Equia", "Consultoría", "Alianza u otra consulta"],
        )
        interes = st.selectbox("Servicio o módulo de interés *", INTEREST_OPTIONS)
        desafio = st.text_area(
            "Desafío principal *",
            max_chars=1200,
            placeholder="Describe brevemente el desafío operacional que quieren abordar. No incluyas información clínica sensible.",
            height=130,
        )
        acepta_contacto = st.checkbox("Acepto ser contactado para responder esta solicitud. *")
        submitted = st.form_submit_button("Enviar solicitud", use_container_width=True)

    if submitted:
        payload = {
            "nombre": nombre,
            "institucion": institucion,
            "cargo": cargo,
            "correo": correo,
            "telefono": telefono,
            "tipo_solicitud": tipo_solicitud,
            "interes": interes,
            "desafio": desafio,
            "acepta_contacto": acepta_contacto,
        }
        errors = validate_contact(payload)
        if errors:
            st.error("Revisa los campos obligatorios y el formato del correo antes de continuar.")
            for message in dict.fromkeys(errors.values()):
                st.caption(f"• {message}")
        else:
            fingerprint = contact_fingerprint(payload)
            if st.session_state.get("last_contact_fingerprint") == fingerprint:
                st.warning("Esta misma solicitud ya fue procesada en esta sesión.")
            else:
                webhook_url = get_config_value("CONTACT_WEBHOOK_URL")
                result = deliver_contact(payload, webhook_url)
                st.session_state["last_contact_fingerprint"] = fingerprint
                if result.delivered:
                    st.success(result.message)
                elif result.ok:
                    st.info(result.message)
                else:
                    st.error(result.message)

st.markdown(
    f"""
    <footer class="site-footer">
      <div><span class="footer-dot"></span><strong>{SITE['consultancy_name']}</strong><p>Experiencia clínica y tecnología para transformar la gestión en salud.</p></div>
      <div><small>EXPLORAR</small><a href="#servicios">Servicios</a><a href="#equia">Equia</a><a href="#equipo">Equipo</a></div>
      <div><small>PENDIENTE</small><a href="#">Privacidad</a><a href="#">Términos de uso</a><a href="#">LinkedIn</a></div>
      <div class="footer-bottom"><span>© [AÑO] {SITE['consultancy_name']}</span><span>Textos legales pendientes de revisión.</span></div>
    </footer>
    """,
    unsafe_allow_html=True,
)

# Los enlaces HTML cambian el hash del documento, pero Streamlit desplaza un
# contenedor interno. Este puente usa los IDs semánticos del sitio y el
# identificador estable del área principal de Streamlit.
st.html(
    """
    <script>
    const host = document;
    if (!host.documentElement.dataset.consultoraNavReady) {
      host.documentElement.dataset.consultoraNavReady = "true";
      host.addEventListener("click", (event) => {
        const link = event.target.closest('a[href^="#"]');
        if (!link) return;
        const target = host.querySelector(link.getAttribute("href"));
        if (!target) return;
        const main = host.querySelector('[data-testid="stMain"]');
        if (!main) return;
        event.preventDefault();
        const top = target.getBoundingClientRect().top - main.getBoundingClientRect().top + main.scrollTop - 96;
        main.scrollTo({ top, behavior: "smooth" });
      }, true);
    }
    </script>
    """,
    unsafe_allow_javascript=True,
)
