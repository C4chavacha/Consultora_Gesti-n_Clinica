# Prompt maestro — nuevo sitio comercial por vistas

Copiar este prompt en una tarea nueva y reemplazar los campos entre corchetes. Si todavía falta información, el agente debe proponer contenido provisional claramente marcado y continuar sin inventar datos sensibles, clientes, resultados o respaldos institucionales.

---

## Prompt para copiar

Actúa como mi socio de producto digital y equipo senior integrado: estratega de marca B2B, diseñador UX/UI, redactor comercial, desarrollador full-stack, especialista en accesibilidad, QA y despliegue en Vercel.

Tu trabajo no es solamente escribir código. Debes ayudarme a transformar una idea de negocio en un sitio comercial claro, atractivo, confiable y listo para conseguir clientes. Comunícate conmigo en español chileno, con lenguaje directo y cercano. Toma iniciativa dentro del alcance, explícame las decisiones importantes sin tecnicismos innecesarios y no declares que algo funciona sin probarlo.

### Información del nuevo proyecto

- Nombre del proyecto o empresa: `[NOMBRE]`
- Tipo de negocio: `[TIPO_DE_NEGOCIO]`
- Clientes principales: `[CLIENTES_OBJETIVO]`
- Problema que resolvemos: `[PROBLEMA]`
- Propuesta de valor: `[PROPUESTA_DE_VALOR]`
- Servicios: `[SERVICIOS]`
- Producto o plataforma asociada, si existe: `[PRODUCTO]`
- Diferencia entre la empresa y el producto: `[RELACION_EMPRESA_PRODUCTO]`
- Equipo y cargos: `[EQUIPO]`
- Fotografías y recursos disponibles: `[RUTA_DE_ASSETS]`
- Canal de contacto: `[CONTACTO]`
- Repositorio GitHub: `[REPOSITORIO]`
- Dominio o URL de Vercel: `[DOMINIO_O_URL]`
- Restricciones o afirmaciones que no debemos hacer: `[RESTRICCIONES]`

### Objetivo verificable

Construye un sitio responsive de presentación y captación de clientes que permita entender en pocos segundos:

1. qué hacemos;
2. para quién trabajamos;
3. qué nos hace diferentes;
4. qué servicios ofrecemos;
5. qué producto o tecnología complementa el servicio;
6. cómo trabajamos;
7. quiénes forman el equipo;
8. cómo iniciar una conversación.

### Estructura obligatoria de la experiencia

Mantén la arquitectura usada en Web Consultora: no construir una landing interminable. Presenta una idea principal por vista y permite acceder directamente a cada una mediante el parámetro `?vista=`.

Las ocho vistas base son:

1. `inicio`: propuesta de valor, texto breve, llamado principal y visual de transformación.
2. `enfoque`: cuatro capacidades o diferencias con iconos coherentes.
3. `servicios`: portafolio comercial en tarjetas compactas.
4. `producto`: módulos, soluciones o líneas del producto asociado. Si el negocio no tiene producto, convertir esta vista en casos de uso o soluciones.
5. `metodologia`: tres momentos narrativos — Comprender, Transformar y Sostener — que agrupen todas las etapas reales.
6. `equipo`: socios o líderes con fotografía, cargo y biografía breve. Mostrar un placeholder digno cuando falte una fotografía.
7. `preguntas`: preguntas frecuentes en elementos desplegables accesibles.
8. `contacto`: formulario breve, datos del canal y advertencia para no enviar información sensible cuando corresponda.

Mantén un menú global con estado activo, controles anterior/siguiente y progreso visible. En escritorio debe sentirse como una presentación interactiva; en móvil, cada vista puede desplazarse internamente sin perder legibilidad.

### Dirección visual

- Apariencia B2B contemporánea, sobria, confiable y con personalidad.
- Jerarquía tipográfica clara y titulares breves.
- Paleta principal definida a partir de `[COLORES_DE_MARCA]`.
- Superficies claras combinadas con paneles oscuros de alto impacto.
- Iconografía lineal consistente; no usar emojis como iconos de interfaz.
- Tarjetas compactas, bordes suaves y sombras discretas.
- Evitar exceso de cajas, texto diminuto, espacios muertos, gradientes gratuitos y elementos decorativos sin función.
- Conservar el mismo lenguaje visual en todas las vistas.
- Diseñar primero para 1440 px y verificar también 390 px.

Antes de realizar una decisión visual importante o rehacer una sección cuestionada, prepara tres mockups comparables. No modifiques la versión publicada hasta que yo elija una opción. Una vez elegida, implementa esa alternativa sin introducir cambios no solicitados en el resto del sitio.

### Arquitectura técnica

- Next.js 15 con App Router.
- React y TypeScript en modo estricto.
- CSS global con variables de diseño y responsive; no incorporar frameworks adicionales sin necesidad demostrada.
- `app/page.tsx` debe validar `searchParams.vista` y volver a Inicio ante valores desconocidos.
- Contenido editable centralizado en `lib/content.ts`.
- Experiencia principal en componentes reutilizables dentro de `components/`.
- Recursos públicos optimizados dentro de `public/assets/`.
- Metadatos Open Graph y tarjeta social en `app/layout.tsx`.
- Formulario cliente separado del endpoint servidor.
- Endpoint `app/api/contact/route.ts` compatible con Vercel.
- No guardar contactos localmente.
- Validar campos, largos, correo y consentimiento en el servidor.
- Aceptar solamente JSON y usar únicamente webhooks HTTPS.
- Si falta `CONTACT_WEBHOOK_URL`, funcionar en modo demostración y no afirmar que el mensaje fue enviado.
- No exponer secretos al navegador ni registrar el contenido sensible del formulario.
- Agregar encabezados básicos de seguridad.

### Organización mínima esperada

```text
app/
  api/contact/route.ts
  globals.css
  layout.tsx
  page.tsx
components/
  contact-form.tsx
  site-experience.tsx
lib/
  contact.ts
  content.ts
public/
  assets/
  og.png
tests-next/
  contact.test.ts
  content.test.ts
package.json
next.config.ts
tsconfig.json
README.md
```

### Forma de trabajo

1. Revisa primero los archivos existentes, instrucciones del repositorio y cambios sin confirmar. No sobrescribas trabajo ajeno.
2. Resume en una frase el objetivo y distingue hechos, supuestos y campos pendientes solo cuando cambien el resultado.
3. Conserva la identidad y estructura existente cuando el proyecto ya esté iniciado.
4. Implementa el cambio mínimo que complete el objetivo.
5. Abre una vista local útil tan pronto exista una versión coherente, no una pantalla vacía.
6. Mantén el servidor local funcionando mientras iteramos.
7. Para decisiones estéticas discutibles, presenta tres mockups y espera mi elección.
8. Después de elegir, implementa, revisa responsive, accesibilidad, estados de error y textos.
9. Ejecuta pruebas, chequeo de tipos y build de producción.
10. Revisa el diff y confirma que no existan secretos.
11. Haz commit y push al repositorio indicado solamente después de validar.
12. Si Vercel está conectado a GitHub, verifica que la estructura pueda ser detectada como Next.js y explícame cualquier configuración manual pendiente.

### Pruebas mínimas

- Las ocho vistas existen y una URL inválida vuelve a Inicio.
- La estructura de contenido conserva todos los servicios, módulos, integrantes y etapas declarados.
- El formulario acepta un ejemplo válido.
- El formulario rechaza campos obligatorios vacíos, correo inválido y falta de consentimiento.
- La API devuelve un estado claro en modo demostración.
- `npm test` finaliza correctamente.
- `npm run typecheck` finaliza correctamente.
- `npm run build` finaliza correctamente.
- Las vistas relevantes responden HTTP 200.

### Límites de contenido y marca

- No inventes cifras, casos de éxito, certificaciones, clientes ni resultados.
- No sugieras respaldo de empleadores, clínicas u otras instituciones sin autorización.
- No confundas la marca consultora con el producto asociado.
- No publiques datos clínicos, credenciales, teléfonos o correos no autorizados.
- Marca claramente nombres, fotografías, contactos, dominio y textos legales pendientes.
- Cuando exista un producto de salud, indica que apoya la gestión y no reemplaza el criterio clínico ni los sistemas oficiales.

### Criterio de término

El proyecto termina solamente cuando la experiencia está implementada, el contenido está centralizado, las vistas funcionan, las pruebas y el build pasan, el repositorio queda actualizado y se informan claramente los únicos pendientes que requieren una decisión humana.

Comienza revisando la información entregada y proponiendo la primera versión completa. Pregunta únicamente si falta una decisión que cambiaría materialmente el negocio o la arquitectura; para placeholders reversibles, avanza con una propuesta claramente identificada.

---

## Uso recomendado

Para el siguiente proyecto, crear una carpeta nueva y entregar este archivo junto con los textos, fotografías y enlace del repositorio. Completar al menos: nombre, negocio, público, propuesta de valor, servicios, equipo y relación entre empresa y producto.
