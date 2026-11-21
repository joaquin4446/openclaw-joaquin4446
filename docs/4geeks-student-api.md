# Mi Asistente 4Geeks
## Integración de OpenClaw con BreatheCode Student API

### Descripción

Proyecto académico desarrollado para integrar un
asistente OpenClaw personalizado, Tidus, con la
API educativa de 4Geeks Academy (BreatheCode).

El objetivo es consultar información académica
y recursos educativos mediante skills reutilizables.

### Tecnologías utilizadas

- OpenClaw 2026.10.9
- Python 3.10
- BreatheCode REST API
- JSON
- Git y GitHub
- Linux VPS

No se instalaron dependencias externas de Python.

### Skills desarrolladas

| Skill | Funcionalidad | Estado |
|---|---|---|
| 4geeks-authenticate | Validación de autenticación | Validada en terminal |
| 4geeks-projects | Consulta de proyectos y estados | Validada en terminal |
| 4geeks-pending-work | Tareas pendientes y rechazadas | Validada en terminal |
| 4geeks-progress-summary | Resumen de estados académicos | Validada en terminal |
| 4geeks-upcoming-events | Consulta de eventos próximos | Validada en terminal |
| 4geeks-learning-resources | Búsqueda de recursos educativos | Validada en terminal |

### Endpoints utilizados

Todos los endpoints son de solo lectura.

Base URL:
https://breathecode.herokuapp.com

- GET /v1/admissions/user/me
- GET /v1/assignment/user/me/task
- GET /v1/events/all
- GET /v1/registry/asset

### Seguridad

Las consultas autenticadas utilizan:

Authorization: Token <credencial>

La credencial real no se almacena en los scripts,
en los archivos SKILL.md ni en Git.

Se registró FOURGEEKS_STUDENT_TOKEN como secreto
protegido de OpenClaw, restringido al dominio
breathecode.herokuapp.com.

Las pruebas de terminal utilizaron una entrada oculta
del token.

La integración automática con el proxy de salida
protegido de OpenClaw todavía no ha sido validada.

### Instalación de las skills

Las seis carpetas deben estar ubicadas en:

~/.openclaw/workspace/skills/

Cada skill contiene:

- SKILL.md: instrucciones y metadatos.
- scripts/*.py: implementación de la consulta.

Para verificar su reconocimiento:

openclaw skills check

Para consultar una skill específica:

openclaw skills info 4geeks-projects

### Pruebas realizadas

Autenticación:
- HTTP 200
- Token válido para el endpoint de usuario.

Proyectos:
- 21 proyectos recuperados.
- 20 con estado DONE.
- 1 con estado PENDING.

Actividades pendientes:
- 9 pendientes.
- 8 ejercicios y 1 proyecto.
- 0 rechazadas.

Resumen de tareas:
- 110 tareas accesibles.
- 101 DONE.
- 9 PENDING.

Eventos:
- 1 evento recuperado en la consulta general.
- Paginación no verificada.
- Academia del evento: 4Geeks.com.

Recursos educativos:
- 95 ejercicios recuperados.
- 21 coincidencias para la búsqueda "python".

Estos resultados corresponden al momento
de las pruebas y pueden cambiar.

### Limitaciones conocidas

1. La consulta de cohortes devolvió HTTP 403.
2. El endpoint de actividad devolvió HTTP 403.
3. La consulta de certificados devolvió HTTP 403.
4. El resumen de tareas no representa el porcentaje
   oficial de progreso académico.
5. DONE no significa necesariamente APPROVED.
6. Los eventos generales no implican inscripción
   del estudiante.
7. La búsqueda de recursos corresponde al catálogo
   general, no al plan personal del estudiante.
8. La ejecución conversacional con Tidus no pudo
   validarse por agotamiento del presupuesto LiteLLM.
9. El acceso automático al secreto protegido desde
   las skills todavía no se ha probado.

### Metodología de desarrollo

Las skills fueron diseñadas con acompañamiento
externo y comprobadas mediante consultas reales
desde la terminal.

El agente Tidus no ejecutó estas pruebas de forma
conversacional debido a la restricción del proveedor
de modelos de IA.

No se atribuyen al agente acciones que no realizó.

### Documentación de evidencias

El archivo SKILL_LOG.md contiene:

- Motivación de cada skill.
- Inputs y outputs.
- Endpoints utilizados.
- Problemas identificados.
- Correcciones realizadas.
- Pruebas y resultados.
- Limitaciones pendientes.

### Repositorio

Rama de desarrollo:
feature/4geeks-student-api-skills

Este proyecto forma parte de la personalización
del asistente OpenClaw Tidus.
