# SKILLS DESIGN — Tidus

## Mi Agente, A Mi Manera

**Proyecto:** 4Geeks Academy — AI Engineering  
**Agente:** Tidus  
**Plataforma:** OpenClaw  
**Integraciones:** Zapier, Google Docs, Google Calendar y Telegram.

## Introducción

Tidus es un asistente personal inteligente diseñado para contribuir a mi formación tecnológica, mejorar mi productividad y facilitar la organización de mis responsabilidades académicas y profesionales.

Las siguientes skills fueron seleccionadas porque responden a necesidades recurrentes de mi rutina y aprovechan las integraciones disponibles, sin requerir nuevas APIs ni conexiones externas.

---

## Skill 1 — Learning Journal

**Identificador:** `learning-journal`

### 1. ¿Qué hace esta skill?

Transforma mis aprendizajes, avances y dificultades académicas en un diario de conocimiento estructurado, guardado automáticamente en Google Docs cuando solicito registrar una sesión.

### 2. ¿Qué input necesita el agente?

El usuario proporciona una descripción breve de lo aprendido, mediante lenguaje natural.

Puede incluir:

- Tema estudiado.
- Proyecto desarrollado.
- Conceptos aprendidos.
- Dificultades encontradas.
- Resultados obtenidos.
- Actividades pendientes.

No es necesario proporcionar todos los campos.

A partir de USER.md, Tidus conoce mi formación en AI Engineering, los proyectos tecnológicos actuales, mis preferencias de aprendizaje y mis objetivos profesionales.

A partir de SOUL.md, conoce el estilo de comunicación y organización que debe utilizar.

AGENTS.md establece las reglas de seguridad y autorización.

Las convenciones de herramientas están documentadas en TOOLS.md y reflejadas en AGENTS.md.

### 3. ¿Cómo es un buen output?

Un documento de Google Docs en español, con el siguiente título:

Diario de aprendizaje | AAAA-MM-DD | Tema principal

El documento debe contener:

1. Fecha de la sesión.
2. Tema o proyecto trabajado.
3. Resumen del aprendizaje.
4. Conceptos técnicos adquiridos.
5. Aplicaciones prácticas.
6. Dificultades y soluciones identificadas.
7. Logros de la sesión.
8. Próximos pasos.

Cuando no exista información suficiente para completar una sección, el agente debe indicarlo sin inventar experiencias ni resultados.

Una vez creado el documento, Tidus devuelve mediante Telegram un resumen breve y su enlace verificado.

### Herramientas utilizadas

- Google Docs mediante Zapier: buscar y crear documentos.
- Telegram: recibir instrucciones y entregar resultados.

### Flujo de ejecución

1. Identificar la solicitud de registro de aprendizaje.
2. Interpretar y organizar la información recibida.
3. Utilizar el contexto académico de USER.md.
4. Generar una entrada estructurada.
5. Comprobar si existe un documento con el mismo título para evitar duplicados.
6. Crear el documento correspondiente.
7. Verificar el resultado.
8. Entregar un resumen y el enlace mediante Telegram.

### Criterios de éxito

- El usuario puede activar la skill con una instrucción breve.
- El contenido refleja los aprendizajes reales proporcionados.
- El documento existe en Google Docs.
- El enlace corresponde al documento creado.
- La estructura es consistente entre diferentes ejecuciones.
- No se generan duplicados involuntarios.

### Caso de prueba real

Registrar los aprendizajes adquiridos durante el Hito 2 de Nexova Solutions, incluyendo interfaces TypeScript, gestión de colecciones, búsquedas lineales y binarias, scoring y pruebas automatizadas.

### Decisión de diseño

La integración actual de Google Docs permite buscar y crear documentos, pero no añadir contenido a documentos existentes.

Por esta razón, cada sesión de aprendizaje se almacenará en un documento independiente, utilizando títulos estandarizados para facilitar su identificación.

---

## Skill 2 — Weekly Planner

**Identificador:** `weekly-planner`

### 1. ¿Qué hace esta skill?

Organiza mis objetivos académicos y profesionales en un plan semanal priorizado, considerando la disponibilidad de mi calendario y creando bloques de trabajo después de mi aprobación.

### 2. ¿Qué input necesita el agente?

El usuario proporciona mediante lenguaje natural:

- Objetivos de la semana.
- Actividades pendientes.
- Fechas límite conocidas.
- Prioridades especiales.
- Restricciones de disponibilidad, cuando corresponda.

Tidus consulta los eventos existentes en Google Calendar y solicita aclaraciones únicamente cuando falten datos indispensables.

A partir de USER.md, conoce mis objetivos académicos y profesionales, mis proyectos actuales y mi preferencia por trabajar de manera organizada y progresiva.

A partir de SOUL.md, conoce los principios de planificación realista, eficiencia y priorización.

AGENTS.md establece los límites de autorización.

Las convenciones de uso de Google Docs, Google Calendar y Telegram están documentadas en TOOLS.md y AGENTS.md.

### 3. ¿Cómo es un buen output?

Un documento de Google Docs con el título:

Plan semanal | AAAA-MM-DD al AAAA-MM-DD

El documento debe incluir:

1. Objetivos principales.
2. Actividades académicas.
3. Actividades profesionales.
4. Prioridades.
5. Distribución de actividades por día.
6. Bloques de trabajo propuestos.
7. Resultados esperados.
8. Actividades pendientes de confirmación.

Después de presentar la propuesta y recibir autorización del usuario, Tidus guarda el plan y crea los bloques aprobados en Google Calendar.

El agente devuelve mediante Telegram un resumen del plan, el enlace del documento y la relación de eventos creados.

### Herramientas utilizadas

- Google Calendar mediante Zapier: consultar eventos, comprobar disponibilidad y crear eventos.
- Google Docs mediante Zapier: crear y localizar el documento del plan semanal.
- Telegram: recibir objetivos, solicitar aprobación y comunicar resultados.

### Flujo de ejecución

1. Identificar los objetivos de la semana.
2. Determinar las fechas y la zona horaria aplicable.
3. Consultar los compromisos existentes en Google Calendar.
4. Identificar períodos disponibles.
5. Organizar las actividades por prioridad.
6. Preparar una propuesta semanal realista.
7. Presentar el plan al usuario para su aprobación.
8. Crear el documento y los eventos autorizados.
9. Verificar los resultados y evitar duplicados.
10. Entregar un resumen mediante Telegram.

### Criterios de éxito

- El plan considera los compromisos existentes.
- Las prioridades reflejan los objetivos proporcionados.
- Los bloques respetan la disponibilidad del usuario.
- No se crean eventos sin autorización.
- El documento existe en Google Docs.
- Los eventos aprobados aparecen en Google Calendar.
- Tidus informa de cualquier acción que no haya podido completarse.

### Caso de prueba real

Organizar una semana de estudio que incluya el desarrollo de skills personalizadas de OpenClaw, práctica de TypeScript y preparación de reportes profesionales.

### Decisiones de diseño

- No modificar ni eliminar eventos existentes.
- No crear eventos con invitados sin autorización.
- No asumir horarios laborales ni disponibilidad no confirmada.
- Verificar nuevamente la disponibilidad antes de crear los eventos aprobados.
- No crear documentos ni eventos duplicados.
- Utilizar exclusivamente las integraciones existentes.

---

## Justificación de las skills seleccionadas

Learning Journal permite construir un registro organizado de los conocimientos adquiridos durante mi formación como AI Engineer.

Weekly Planner facilita la organización de mis responsabilidades académicas y profesionales, convirtiendo objetivos generales en actividades concretas.

Ambas skills resuelven tareas recurrentes, aprovechan la personalización de Tidus y utilizan herramientas ya disponibles en OpenClaw mediante Zapier.

## Seguridad y privacidad

Las skills deben respetar las reglas de AGENTS.md, proteger la información privada, utilizar únicamente servicios autorizados y verificar los resultados antes de afirmar que una acción fue completada.

## Estado del diseño

Diseño previo a la implementación.

Las skills serán implementadas individualmente y sometidas a pruebas reales después de registrar este documento mediante un commit en Git.
