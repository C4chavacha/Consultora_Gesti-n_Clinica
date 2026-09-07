# Web Consultora

Landing comercial en Streamlit para una consultora de gestión clínica, transformación operacional, inteligencia de negocios e innovación en salud. La consultora se presenta como marca principal y **Equia** como su plataforma tecnológica modular.

## Estado de esta versión

- Landing responsive con navegación por secciones.
- Servicios, módulos de Equia, metodología, equipo y preguntas frecuentes.
- Retratos oficiales integrados para Rodrigo Hernández, Felipe Muñoz y Fabián Cifuentes; Sofía Vergara mantiene un bloque provisional hasta recibir su fotografía.
- Formulario validado con prevención básica de duplicados por sesión.
- Entrega opcional por webhook. Sin configuración, el formulario funciona en modo demostración y no afirma que el mensaje fue enviado.
- Contenedor Docker y configuración compatible con Streamlit Community Cloud.

## Instalación local

Requiere Python 3.12 o una versión compatible con las dependencias declaradas.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

Abra `http://localhost:8501`.

## Configuración del formulario

El formulario no guarda datos localmente. Para activar una entrega real:

1. Copie `.streamlit/secrets.toml.example` como `.streamlit/secrets.toml`.
2. Configure `CONTACT_WEBHOOK_URL` con una URL HTTPS que reciba JSON por `POST`.
3. Pruebe el flujo completo con datos ficticios antes de publicar.

También puede definirse la variable de entorno `CONTACT_WEBHOOK_URL`. Las variables de entorno tienen prioridad sobre `st.secrets`.

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
python -m unittest discover -s tests -v
```

Las pruebas cubren render inicial, validación correcta e incorrecta, modo demostración, huella de duplicados y confirmación de entrega mediante webhook.

## Despliegue en Streamlit Community Cloud

1. Publique esta carpeta en un repositorio Git.
2. Cree una aplicación y seleccione `app.py` como archivo principal.
3. Agregue `CONTACT_WEBHOOK_URL` en la sección de secretos de la plataforma.
4. Revise el sitio completo y el formulario antes de enlazar un dominio o difundirlo.

Esta alternativa simplifica una demostración inicial. Revise las capacidades vigentes de dominio, privacidad y operación de la plataforma antes de elegirla para producción.

## Despliegue con Docker

```powershell
docker build -t web-consultora .
docker run --rm -p 8501:8501 -e CONTACT_WEBHOOK_URL="https://ejemplo" web-consultora
```

Un servicio que ejecute contenedores puede publicar esta imagen y conectar posteriormente un dominio propio. Configure HTTPS, secretos administrados, monitoreo, protección contra abuso y una política formal de datos antes de producción.

## Analítica

`ANALYTICS_MEASUREMENT_ID` queda reservado para una integración futura. Esta versión no carga servicios externos de analítica ni cookies. Antes de activarlos, defina consentimiento, política de privacidad y criterios de minimización de datos.

## Actualización de contenidos

- Textos y listas: `content.py`.
- Estilos y responsive: `styles/site.css`.
- Entrega del formulario: `services/contact_service.py`.
- Marca Equia y tarjeta social: `assets/`.

Las fotografías web optimizadas están en `assets/team/`. Los originales se conservan localmente en `FotosDirectores/`, carpeta excluida del repositorio. La asociación de cada imagen se administra en `TEAM`, dentro de `content.py`. Use encuadre, iluminación y proporciones consistentes para futuras incorporaciones.

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
