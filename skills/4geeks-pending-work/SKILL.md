---
name: 4geeks-pending-work
description: Consulta las actividades pendientes y rechazadas del estudiante de 4Geeks mediante la API BreatheCode.
user-invocable: true
---

# 4Geeks Pending Work

## Objetivo

Identificar las actividades académicas que están pendientes
o rechazadas y necesitan atención del estudiante.

## Cuándo utilizar

Cuando el usuario pregunte:

- ¿Qué me falta por entregar en 4Geeks?
- ¿Qué tareas tengo pendientes?
- ¿Tengo actividades rechazadas?
- ¿Qué ejercicios debo completar?
- Muéstrame mi trabajo pendiente.

## Endpoint

GET https://breathecode.herokuapp.com/v1/assignment/user/me/task

Filtros utilizados:

- task_status=PENDING
- task_status=REJECTED
- limit=50
- offset para paginación

## Procedimiento

1. Consultar las tareas con estado PENDING.
2. Consultar las tareas con estado REJECTED.
3. Recuperar todas las páginas de cada consulta.
4. Ejecutar el script desde el workspace:

   python3 -B skills/4geeks-pending-work/scripts/list_pending.py

5. Interpretar el JSON obtenido.
6. Presentar por separado las tareas pendientes
   y las rechazadas.
7. Mostrar títulos, tipos y estados disponibles.
8. Informar los errores de acceso o paginación.

## Autenticación

El script utiliza FOURGEEKS_STUDENT_TOKEN cuando
está disponible en un entorno autorizado.

No asumir que el secreto almacenado en OpenClaw
se inyecta automáticamente en el script.

No solicitar tokens mediante Telegram ni
incluir credenciales en comandos o registros.

## Output esperado

Respuesta en español con:

- Cantidad de actividades pendientes.
- Cantidad de actividades rechazadas.
- Distribución por tipo de tarea.
- Lista de tareas que requieren atención.

## Reglas

- PENDING significa pendiente según la API.
- REJECTED significa rechazada según la API.
- DONE no implica aprobación.
- No inferir un porcentaje oficial de avance.
- No afirmar que no existen actividades pendientes
  si alguna consulta falló.
- No marcar tareas como terminadas.
- No enviar entregas.
- No modificar información del estudiante.
- No inventar resultados.
- Respetar AGENTS.md.

## Limitaciones

Las pruebas desde SSH validan el funcionamiento
técnico, pero no la ejecución conversacional.

La prueba desde Telegram y el acceso automático
al secreto protegido siguen pendientes.
