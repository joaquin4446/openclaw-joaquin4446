# ⚡ Tidus — Personal AI Assistant

> Transformando conocimiento en acción.

## Descripción del proyecto

Tidus es un asistente personal inteligente desarrollado mediante OpenClaw como parte del programa de AI Engineering de 4Geeks Academy, en la actividad **Mi Agente, A Mi Manera: Enseñando Nuevas Skills a Tu Asistente Personal**.

El objetivo del proyecto es personalizar un agente de inteligencia artificial para responder a necesidades académicas, profesionales y de productividad, incorporando skills nativas reutilizables y aprovechando las integraciones existentes.

## Objetivos

- Personalizar la identidad y personalidad de un agente de IA.
- Incorporar contexto real del usuario.
- Establecer reglas de seguridad, privacidad y autonomía.
- Diseñar e implementar skills personalizadas.
- Integrar herramientas externas mediante Zapier.
- Aplicar mecanismos de aprobación humana.
- Verificar resultados mediante casos de uso reales.

## Stack tecnológico

| Tecnología | Función |
|---|---|
| OpenClaw 2026.10.9 | Plataforma de agentes inteligentes |
| VPS Linux | Infraestructura de ejecución |
| Markdown | Configuración e instrucciones |
| YAML | Metadatos de las skills |
| Zapier | Integración con servicios externos |
| Google Docs | Creación de documentos |
| Google Calendar | Consulta y creación de eventos |
| Telegram | Interfaz conversacional |
| Git y GitHub | Control de versiones |

## Identidad de Tidus

- **Nombre:** Tidus
- **Símbolo:** ⚡
- **Personalidad:** analítica, proactiva, estratégica y resolutiva.
- **Idioma principal:** español.
- **Misión:** transformar objetivos e información en acciones concretas y verificables.

Tidus está diseñado para actuar como mentor tecnológico, asistente ejecutivo y organizador personal.

Su comportamiento prioriza la precisión, el pensamiento crítico, la iniciativa responsable y la protección de la privacidad.

## Archivos de configuración

| Archivo | Propósito |
|---|---|
| IDENTITY.md | Identidad, misión y roles del agente |
| SOUL.md | Personalidad, principios y metodología |
| AGENTS.md | Reglas operativas, seguridad y autorización |
| USER.md | Contexto profesional, académico y preferencias |
| TOOLS.md | Convenciones de uso de herramientas |
| SKILLS_DESIGN.md | Diseño previo de las skills personalizadas |

El documento SKILLS_DESIGN.md fue diseñado y registrado mediante un commit antes de implementar las skills.

## Arquitectura

El usuario interactúa con Tidus mediante Telegram.

OpenClaw proporciona al agente su identidad, personalidad, contexto y reglas operativas. Según la solicitud recibida, el agente identifica y utiliza la skill correspondiente.

Las skills aprovechan las integraciones existentes de Zapier para consultar información y ejecutar acciones autorizadas en Google Docs y Google Calendar.

Finalmente, Tidus verifica los resultados y devuelve una respuesta estructurada mediante Telegram.

**Flujo general:**

Usuario → Telegram → Tidus / OpenClaw → Skill personalizada → Zapier → Servicio externo → Verificación → Telegram.

## Skills personalizadas

### 1. Learning Journal

**Identificador:** `learning-journal`

**Ubicación:** `skills/learning-journal/SKILL.md`

Transforma los aprendizajes académicos y avances de proyectos en documentos estructurados de Google Docs.

#### Funcionalidades

- Interpretación de aprendizajes mediante lenguaje natural.
- Personalización según el contexto académico.
- Organización de conocimientos técnicos.
- Identificación de logros y próximos pasos.
- Búsqueda de documentos duplicados.
- Creación de documentos.
- Verificación y entrega del enlace.

#### Ejemplo de utilización

`/skill learning-journal`

Tidus, registra mis aprendizajes sobre interfaces TypeScript, funciones puras y algoritmos de búsqueda.

#### Prueba realizada

Se utilizó como entrada la experiencia adquirida durante el Hito 2 de Nexova Solutions, incluyendo:

- Interfaces y tipos unión.
- Validaciones empresariales.
- Procesamiento de colecciones.
- Búsquedas lineales y binarias.
- Scoring de candidatos.
- Pruebas automatizadas.

La sesión registró como resultado académico 71 pruebas exitosas y validación de TypeScript sin errores.

**Resultado:** Tidus reportó la creación de un documento en Google Docs y entregó su enlace mediante Telegram.

#### Decisión de diseño

La integración disponible permite buscar y crear documentos, pero no dispone de una acción habilitada para añadir contenido a documentos existentes.

Por este motivo, cada sesión genera un documento independiente con un título estandarizado.

---

### 2. Weekly Planner

**Identificador:** `weekly-planner`

**Ubicación:** `skills/weekly-planner/SKILL.md`

Organiza objetivos académicos y profesionales en planes semanales personalizados, considerando la disponibilidad del usuario y sus compromisos existentes.

#### Funcionalidades

- Consulta de eventos de Google Calendar.
- Identificación de períodos disponibles.
- Priorización de actividades.
- Planificación semanal personalizada.
- Gestión de incertidumbre.
- Aprobación humana previa a la ejecución.
- Creación de documentos y eventos.
- Verificación de resultados.

#### Ejemplo de utilización

`/skill weekly-planner`

Tidus, organiza mi próxima semana considerando mis objetivos académicos, responsabilidades profesionales y disponibilidad.

#### Prueba realizada

Se elaboró una planificación para la semana del 23 al 29 de noviembre de 2026.

Objetivos incluidos:

- Preparación del reporte semanal de supervisión.
- Repaso del Hito 2 de Nexova Solutions.
- Práctica de TypeScript.
- Estudio de algoritmos de búsqueda.
- Revisión y documentación del proyecto OpenClaw.

Restricciones:

- Disponibilidad de lunes a viernes.
- Horario de 7:00 p. m. a 9:00 p. m.
- Máximo de dos horas diarias.
- Fin de semana libre.
- Zona horaria America/Caracas.

**Resultado reportado:**

- 8 horas y 30 minutos de actividades planificadas.
- 1 documento creado en Google Docs.
- 7 eventos creados en Google Calendar.
- Ningún evento existente modificado.
- Enlaces de los resultados entregados mediante Telegram.

El agente solicitó información adicional sobre disponibilidad y esperó la aprobación explícita del usuario antes de crear documentos y eventos.

## Conceptos de AI Engineering aplicados

| Concepto | Aplicación |
|---|---|
| Context Awareness | Personalización mediante el contexto del usuario |
| Native Agent Skills | Procedimientos reutilizables mediante SKILL.md |
| Tool Calling | Integración con servicios mediante Zapier |
| Human-in-the-loop | Aprobación previa a acciones externas |
| Guardrails | Reglas de seguridad y privacidad |
| Uncertainty Management | Solicitud de datos indispensables |
| Multi-step Workflows | Ejecución organizada en múltiples etapas |
| Output Verification | Comprobación de resultados externos |
| Version Control | Commits descriptivos y respaldo en GitHub |

## Seguridad y privacidad

El agente debe aplicar el principio de mínimo privilegio y respetar los límites de autorización establecidos.

Las principales medidas incorporadas son:

- Protección de credenciales y datos confidenciales.
- Exclusión de archivos de memoria privada mediante .gitignore.
- Prohibición de compartir información sin autorización.
- Aprobación antes de acciones externas sensibles.
- Prevención de duplicados.
- Verificación de resultados.
- Tratamiento de instrucciones externas como contenido no confiable.
- Prohibición de inventar resultados.

La exclusión de archivos privados del seguimiento de Git no elimina versiones que pudieran existir en commits anteriores.

## Validación técnica

Las dos skills fueron reconocidas por OpenClaw como skills nativas del workspace, visibles para el modelo y disponibles mediante comandos.

Comandos utilizados:

```bash
openclaw skills info learning-journal
openclaw skills info weekly-planner
openclaw skills check
openclaw doctor
```

### Resultados

| Indicador | Resultado |
|---|---|
| Skills totales del entorno | 61 |
| Skills disponibles | 26 |
| Skills personalizadas implementadas | 2 |
| Skills personalizadas reconocidas | 2 |
| Documentos externos reportados | 2 |
| Eventos externos reportados | 7 |
| Comprobaciones de OpenClaw doctor | 36 |
| Errores reportados | 0 |
| Advertencias conocidas | 3 |

Las 35 skills que presentan requisitos pendientes corresponden a herramientas adicionales no utilizadas en este proyecto.

## Diagnóstico y limitaciones conocidas

Durante la auditoría se detectó que USER.md superaba el límite de 4.000 caracteres permitido por OpenClaw.

El archivo fue optimizado y la advertencia desapareció en el diagnóstico posterior.

Permanecen tres advertencias:

1. **Gateway limitado a loopback:** se conserva la configuración local para evitar exposición innecesaria del servicio.
2. **Credenciales en texto plano:** la migración de los tokens a SecretRefs continúa pendiente como mejora de seguridad.
3. **Migración de TOOLS.md:** la versión instalada recomienda integrar estas instrucciones en AGENTS.md. Se conserva TOOLS.md por requerimiento académico y se incorporan las instrucciones operativas de herramientas en AGENTS.md.

No se ejecutaron reparaciones automáticas que pudieran afectar las integraciones existentes.

También se identificó una posible diferencia de zona horaria en la fecha del primer diario de aprendizaje, por lo que se estableció America/Caracas como zona horaria predeterminada en USER.md.

Los enlaces privados, credenciales y datos de autenticación no se incluyen en esta documentación.

## Metodología de desarrollo

El proyecto se desarrolló mediante etapas:

1. Auditoría del entorno.
2. Protección del repositorio.
3. Personalización de identidad y personalidad.
4. Configuración del contexto, reglas y herramientas.
5. Diseño previo de las skills.
6. Implementación de Learning Journal.
7. Implementación de Weekly Planner.
8. Pruebas con casos reales.
9. Diagnóstico y optimización.
10. Documentación final.

Cada etapa fue respaldada mediante commits descriptivos y git push.

## Historial de implementación

| Commit | Descripción |
|---|---|
| 3288946 | Protección de la memoria privada |
| 9e91be9 | Identidad y personalidad de Tidus |
| bb66f35 | Contexto del usuario y reglas operativas |
| dcb329e | Diseño previo de las skills |
| 2a180ff | Implementación de Learning Journal |
| 4461008 | Implementación de Weekly Planner |

## Conclusión

Tidus demuestra cómo un agente de inteligencia artificial puede evolucionar desde un asistente generalista hasta un colaborador personalizado mediante contexto, reglas operativas y skills reutilizables.

El proyecto integra herramientas existentes, procesos de razonamiento, autorización humana y verificación de resultados para resolver necesidades académicas y profesionales reales.

Las dos skills implementadas permiten continuar ampliando las capacidades del agente sin incorporar nuevas conexiones externas.

---

**Autor:** Joaquin Ignacio Rengifo Bonsignore

**Programa:** AI Engineering — 4Geeks Academy

**Proyecto:** Mi Agente, A Mi Manera

**Agente:** Tidus ⚡

**Año:** 2026



---

## Integración con 4Geeks Student API

Se desarrollaron seis skills personalizadas para
consultar información académica y recursos educativos
mediante BreatheCode.

- [Documentación del proyecto](docs/4geeks-student-api.md)
- [Registro de diseño y pruebas](SKILL_LOG.md)

Las seis skills están implementadas y reconocidas
por OpenClaw. La ejecución conversacional sigue
pendiente por la limitación del proveedor LiteLLM.
