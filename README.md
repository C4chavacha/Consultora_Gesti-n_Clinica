# Web Consultora

Sitio comercial en Next.js para una consultora de gestión clínica, transformación operacional, inteligencia de negocios e innovación en salud. La consultora se presenta como marca principal y **Equia** como su plataforma tecnológica modular.

## Estado de esta versión

- Aplicación Next.js 15 lista para desplegar en Vercel.
- Experiencia responsive organizada en ocho vistas enfocadas, sin una landing continua.
- Navegación directa por URL, estado activo y controles anterior/siguiente.
- Servicios, módulos de Equia, metodología, equipo y preguntas frecuentes.
- Retratos oficiales integrados para Rodrigo Hernández, Felipe Muñoz y Fabián Cifuentes; Sofía Vergara mantiene un bloque provisional hasta recibir su fotografía.
- Formulario validado con prevención básica de duplicados por sesión.
- Entrega opcional por webhook. Sin configuración, el formulario funciona en modo demostración y no afirma que el mensaje fue enviado.
- Endpoint interno `/api/contact` compatible con las funciones de Vercel.

## Instalación local

Requiere Node.js 20 o superior.

```powershell
npm install
npm run dev
```

Abra `http://localhost:3000`.

## Configuración del formulario

El formulario no guarda datos localmente. Para activar una entrega real:

1. Configure `CONTACT_WEBHOOK_URL` en las variables de entorno de Vercel con una URL HTTPS que reciba JSON por `POST`.
2. Opcionalmente defina `NEXT_PUBLIC_SITE_URL` con el dominio público para los metadatos sociales.
3. Pruebe el flujo completo con datos ficticios antes de publicar.

Si no existe una URL configurada, la interfaz avisa que está en **modo demostración** y confirma solamente que los datos fueron validados, no enviados.

Campos JSON enviados:

- `nombre`
- `institucion`
- `cargo`
- `correo`
- `telefono`
- `tipo_solicitud`
- `interes`
- `desafio`
- `acepta_contacto`

Antes de integrar un CRM, agregue autenticación del webhook, limitación de frecuencia en el servidor, política de retención y avisos de privacidad revisados legalmente.

## Pruebas

```powershell
npm test
npm run typecheck
npm run build
```

Las pruebas automatizadas cubren las ocho vistas, fallback de rutas inválidas, módulos de Equia y validación correcta e incorrecta del contacto. La validación HTTP comprueba además las ocho respuestas públicas, el rechazo de solicitudes incompletas y el modo demostración.

## Despliegue en Vercel

1. Importe en Vercel el repositorio `C4chavacha/Consultora_Gesti-n_Clinica`.
2. Framework Preset: **Next.js**. Root Directory: `.`.
3. Mantenga Build Command e Install Command con los valores automáticos de Next.js.
4. Agregue `CONTACT_WEBHOOK_URL` solo cuando exista un canal productivo revisado.
5. Despliegue y pruebe las ocho vistas y el formulario antes de conectar el dominio.

## Analítica

`ANALYTICS_MEASUREMENT_ID` queda reservado para una integración futura. Esta versión no carga servicios externos de analítica ni cookies. Antes de activarlos, defina consentimiento, política de privacidad y criterios de minimización de datos.

## Actualización de contenidos

- Textos y listas: `lib/content.ts`.
- Estilos y responsive: `app/globals.css`.
- Entrega del formulario: `app/api/contact/route.ts` y `lib/contact.ts`.
- Marca Equia y tarjeta social: `public/assets/` y `public/og.png`.

Las fotografías web optimizadas están en `public/assets/team/`. Los originales se conservan localmente en `FotosDirectores/`, carpeta excluida del repositorio. La asociación de cada imagen se administra en `team`, dentro de `lib/content.ts`. Use encuadre, iluminación y proporciones consistentes para futuras incorporaciones.

## Respaldo de la versión anterior

Los archivos de Streamlit (`app.py`, `content.py`, `services/`, `styles/` y `tests/`) se mantienen temporalmente como referencia y rollback. Vercel detecta `package.json` y publica la aplicación Next.js.

## Placeholders pendientes

- `[NOMBRE DE LA CONSULTORA]`
- fotografía oficial de Sofía Vergara;
- correo y teléfono corporativos;
- dominio y LinkedIn;
- año del pie de página;
- política de privacidad y términos revisados;
- canal real de contacto;
- logotipo definitivo de la consultora.

## Revisión antes de publicar

- Obtener autorización para nombres, cargos, fotografías y biografías.
- Confirmar marca, dominio y disponibilidad registral.
- No utilizar marcas ni sugerir respaldo de empleadores o instituciones sin autorización formal.
- Revisar los textos legales y el tratamiento de contactos.
- Probar accesibilidad, navegación móvil y formulario en el dominio final.
- Confirmar que módulos y capacidades de Equia coincidan con la versión que se ofrecerá comercialmente.
