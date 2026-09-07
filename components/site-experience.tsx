import Image from "next/image";
import Link from "next/link";
import type { ComponentType } from "react";
import {
  ArrowLeft, ArrowRight, ArrowUpRight, ChartNoAxesCombined, ChartSpline,
  Check, CircleDollarSign, Cpu, GraduationCap, Layers3, LucideProps,
  Route, SearchCheck, Shuffle, Stethoscope, UsersRound, Workflow
} from "lucide-react";
import { ContactForm } from "./contact-form";
import { capabilities, faqs, methodology, methodologyPhases, modules, services, site, team, ViewKey, views } from "@/lib/content";

const icons: Record<string, ComponentType<LucideProps>> = {
  Stethoscope, Workflow, ChartNoAxesCombined, Cpu, SearchCheck, Shuffle,
  UsersRound, Route, ChartSpline, CircleDollarSign, Layers3, GraduationCap
};

function href(view: ViewKey) {
  return `/?vista=${view}`;
}

function Header({ activeView }: { activeView: ViewKey }) {
  return (
    <header className="site-header">
      <Link className="brand" href={href("inicio")} aria-label="Ir al inicio">
        <span className="brand-mark">✦</span><span>{site.consultancyName}</span>
      </Link>
      <nav className="main-nav" aria-label="Navegación principal">
        {views.map((view) => (
          <Link key={view.key} href={href(view.key)} aria-current={view.key === activeView ? "page" : undefined} className={view.key === "contacto" ? "contact-link" : undefined}>
            {view.label}
          </Link>
        ))}
      </nav>
    </header>
  );
}

function SectionIntro({ kicker, title, copy }: { kicker: string; title: React.ReactNode; copy: string }) {
  return (
    <div className="section-intro">
      <span className="kicker">{kicker}</span>
      <div className="section-title"><h1>{title}</h1><p>{copy}</p></div>
    </div>
  );
}

function HomeView() {
  return (
    <div className="home-view">
      <section className="hero-copy">
        <span className="kicker with-line">{site.eyebrow}</span>
        <h1>{site.headline}</h1>
        <p>{site.lead}</p>
        <div className="hero-actions">
          <Link className="button primary" href={href("contacto")}>Agenda una conversación <ArrowUpRight size={17} /></Link>
          <Link className="button secondary" href={href("equia")}>Conoce Equia <ArrowRight size={17} /></Link>
        </div>
      </section>
      <div className="flow-visual" aria-label="Proceso desde el diagnóstico hasta la implementación">
        <div className="visual-head"><span>TRANSFORMACIÓN APLICADA</span><b><i /> EN TERRENO</b></div>
        <div className="flow-steps">
          {[["01", "Diagnóstico", "Comprender"], ["02", "Diseño", "Priorizar"], ["03", "Implementación", "Transformar"]].map(([number, title, verb], index) => (
            <div className="flow-item" key={number}>
              <div className="flow-node"><small>{number}</small><strong>{title}</strong><span>{verb}</span></div>
              {index < 2 && <div className="flow-connector"><i /><i /><i /></div>}
            </div>
          ))}
        </div>
        <div className="visual-foot"><span>CLÍNICA</span><span>OPERACIONES</span><span>DATOS</span><span>TECNOLOGÍA</span></div>
      </div>
      <div className="trust-line"><span>Del diagnóstico a la adopción</span><i /><span>Diseño junto a los equipos</span><i /><span>Decisiones trazables</span></div>
    </div>
  );
}

function FocusView() {
  return <>
    <SectionIntro kicker="QUÉ NOS HACE DIFERENTES" title={<>Conocemos la complejidad<br />desde dentro.</>} copy="No entregamos solamente informes o software aislado. Conectamos estrategia, operación y tecnología para acompañar cambios que puedan sostenerse en la práctica." />
    <div className="capability-grid">{capabilities.map((item) => { const Icon = icons[item.icon]; return (
      <article className="capability-card" key={item.number}><div className="card-top"><span className="icon-box"><Icon /></span><b>{item.number}</b></div><h2>{item.title}</h2><p>{item.body}</p></article>
    ); })}</div>
  </>;
}

function ServicesView() {
  return <>
    <SectionIntro kicker="SERVICIOS" title={<>Capacidades para transformar<br />la gestión en salud.</>} copy="Partimos por el desafío real de cada institución y construimos una ruta proporcional a su contexto y madurez operacional." />
    <div className="service-grid">{services.map((item, index) => { const Icon = icons[item.icon]; return (
      <article className="service-card" key={item.title}><div className="card-top"><span className="icon-box"><Icon /></span><b>{String(index + 1).padStart(2, "0")}</b></div><h2>{item.title}</h2><p>{item.body}</p></article>
    ); })}</div>
  </>;
}

function EquiaView() {
  return <>
    <section className="equia-hero">
      <div><span className="kicker light">PLATAFORMA TECNOLÓGICA</span><h1>Equia convierte la estrategia operacional en herramientas concretas.</h1><p>Un ecosistema clínico modular que reúne planificación, gestión operacional, analítica y apoyo a la toma de decisiones.</p></div>
      <div className="equia-brand"><Image src="/assets/equia-mark.png" alt="Marca Equia" width={190} height={190} priority /><small>UNA PLATAFORMA · MÚLTIPLES DESAFÍOS</small></div>
    </section>
    <div className="module-grid">{modules.map((module) => <article className={`module-card ${module.status === "En desarrollo" ? "in-progress" : ""}`} key={module.code}>
      <div className="module-head"><span>{module.code}</span><b>{module.status}</b></div><small>{module.tag}</small><h2>{module.name}</h2><p>{module.body}</p>
    </article>)}</div>
    <p className="product-note">Equia apoya la gestión y la toma de decisiones. No reemplaza el criterio clínico ni los sistemas oficiales de cada institución.</p>
  </>;
}

function MethodView() {
  return <>
    <SectionIntro kicker="METODOLOGÍA" title={<>Tres momentos para<br />convertir estrategia en cambio.</>} copy="Una forma simple de explicar cómo trabajamos: comprender el desafío, transformar la operación y dejar capacidades que puedan sostenerse." />
    <div className="method-phases" aria-label="Metodología en tres momentos">
      {methodologyPhases.map((phase) => (
        <article className="method-phase" key={phase.number}>
          <div className="phase-heading"><span>{phase.number}</span><small>{phase.name}</small></div>
          <h2>{phase.headline}</h2>
          <p>{phase.body}</p>
          <ol>
            {methodology.filter((step) => phase.steps.some((number) => number === step.number)).map((step) => (
              <li key={step.number}><b>{step.number}</b><div><strong>{step.title}</strong><span>{step.body}</span></div></li>
            ))}
          </ol>
        </article>
      ))}
    </div>
  </>;
}

function TeamView() {
  return <>
    <SectionIntro kicker="EQUIPO" title={<>Experiencia ejecutiva<br />puesta al servicio del cambio.</>} copy="Una mirada multidisciplinaria para conectar la práctica clínica, los flujos hospitalarios, la gestión y la tecnología." />
    <div className="team-grid">{team.map((person) => <article className="team-card" key={person.initials}>
      {person.photo ? <div className="portrait"><Image src={person.photo} alt={`Retrato de ${person.name}`} fill sizes="(max-width: 700px) 100vw, 25vw" /></div> : <div className="portrait placeholder"><strong>{person.initials}</strong><small>FOTOGRAFÍA<br />PRÓXIMAMENTE</small></div>}
      <div className="team-copy"><span>{person.role}</span><h2>{person.name}</h2><p>{person.bio}</p></div>
    </article>)}</div>
  </>;
}

function FaqView() {
  return <div className="faq-layout">
    <SectionIntro kicker="PREGUNTAS FRECUENTES" title={<>Respuestas claras<br />antes de comenzar.</>} copy="Si tu desafío no aparece aquí, conversemos. La primera conversación sirve para entender el contexto y definir si podemos aportar." />
    <div className="faq-list">{faqs.map((faq, index) => <details key={faq.question} open={index === 0}><summary><span>{String(index + 1).padStart(2, "0")}</span>{faq.question}<b>+</b></summary><p>{faq.answer}</p></details>)}</div>
  </div>;
}

function ContactView() {
  return <section className="contact-panel">
    <div className="contact-copy"><span className="kicker light">CONVERSEMOS</span><h1>Partamos por el desafío, no por la herramienta.</h1><p>Cuéntanos qué necesitan mejorar. Revisaremos el contexto y coordinaremos una primera conversación sin compromiso.</p>
      <div className="contact-detail"><small>RESPUESTA</small><strong>Canal en preparación · formulario demostrativo</strong></div>
      <div className="contact-detail"><small>ALCANCE</small><strong>Chile · proyectos presenciales, híbridos y remotos</strong></div>
      <p className="sensitive-note">Este formulario no solicita ni debe recibir datos personales de pacientes, fichas clínicas o información sensible.</p>
    </div>
    <ContactForm />
  </section>;
}

const viewComponents: Record<ViewKey, ComponentType> = { inicio: HomeView, enfoque: FocusView, servicios: ServicesView, equia: EquiaView, metodologia: MethodView, equipo: TeamView, preguntas: FaqView, contacto: ContactView };

function ViewControls({ activeView }: { activeView: ViewKey }) {
  const index = views.findIndex((view) => view.key === activeView);
  const previous = index > 0 ? views[index - 1] : null;
  const next = views[index + 1] ?? views[0];
  return <nav className="view-controls" aria-label="Avance entre vistas">
    {previous ? <Link href={href(previous.key)}><ArrowLeft size={16} />{previous.label}</Link> : <span className="disabled">Primera vista</span>}
    <div className="progress"><span>{String(index + 1).padStart(2, "0")} / {String(views.length).padStart(2, "0")}</span><div>{views.map((view, itemIndex) => <i className={itemIndex === index ? "current" : ""} key={view.key} />)}</div></div>
    <Link href={href(next.key)} className="next">{index === views.length - 1 ? "Volver al inicio" : next.label}<ArrowRight size={16} /></Link>
  </nav>;
}

function Footer() {
  return <footer><span><i /> {site.consultancyName}</span><p>Consultoría en gestión clínica, operaciones y tecnología.</p><small>© {new Date().getFullYear()} · Todos los derechos reservados</small></footer>;
}

export function SiteExperience({ activeView }: { activeView: ViewKey }) {
  const ActiveView = viewComponents[activeView];
  return <div className="site-shell"><Header activeView={activeView} /><main key={activeView}><div className="active-view"><ActiveView /></div><ViewControls activeView={activeView} /></main><Footer /></div>;
}
