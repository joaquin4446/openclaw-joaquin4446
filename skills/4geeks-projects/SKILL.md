---
name: 4geeks-projects
description: Consulta todos los proyectos académicos del estudiante de 4Geeks y muestra sus estados mediante BreatheCode.
user-invocable: true
---

# 4Geeks Projects

## Objetivo

Consultar los proyectos académicos asignados al estudiante
y presentar sus estados de manera clara y verificable.

## Cuándo utilizar

Cuando el usuario pregunte:

- ¿Qué proyectos tengo en 4Geeks?
- Muéstrame mis proyectos.
- ¿Cuáles son los estados de mis proyectos?
- ¿Qué proyectos he entregado?

## Endpoint

GET https://breathecode.herokuapp.com/v1/assignment/user/me/task

Parámetros:

- task_type=PROJECT
- limit=50
- offset para paginación

## Procedimiento

1. Utilizar únicamente el endpoint indicado.
2. Ejecutar desde el workspace:

   python3 -B skills/4geeks-projects/scripts/list_projects.py

3. Interpretar el JSON devuelto.
4. Informar la cantidad total de proyectos.
5. Mostrar los títulos y estados de los proyectos.
6. Conservar los estados originales de BreatheCode.
7. No interpretar DONE como APPROVED.
8. No afirmar que todos los proyectos fueron recuperados
   si la consulta devolvió un error de paginación.

## Autenticación

El script acepta FOURGEEKS_STUDENT_TOKEN desde un
entorno de ejecución seguro autorizado.

El secreto almacenado en OpenClaw no equivale
automáticamente a una variable de entorno.

La integración del secreto con el entorno del agente
debe verificarse antes de utilizar esta skill desde Telegram.

No solicitar tokens en conversaciones ni introducir
credenciales mediante argumentos de comandos.

## Output esperado

Respuesta en español con:

- Total de proyectos.
- Cantidades agrupadas por estado.
- Nombre y estado de cada proyecto solicitado.
- Advertencias cuando corresponda.

## Restricciones

- Solo lectura.
- No entregar ni modificar tareas.
- No mostrar credenciales.
- No inventar nombres, estados ni porcentajes.
- No confundir estados de tareas con progreso oficial del curso.
- Respetar AGENTS.md.

## Validación

La prueba desde terminal demuestra la ejecución técnica
del script y su acceso al endpoint.

La prueba conversacional sigue pendiente mientras
el servicio del modelo no esté disponible.
