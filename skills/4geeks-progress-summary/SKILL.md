---
name: 4geeks-progress-summary
description: Genera un resumen académico basado en los estados de las tareas del estudiante de 4Geeks mediante BreatheCode.
user-invocable: true
---

# 4Geeks Progress Summary

## Objetivo

Resumir los estados de las tareas académicas
accesibles mediante la API de BreatheCode.

## Cuándo utilizar

Cuando el usuario pregunte:

- ¿Cómo van mis entregas de 4Geeks?
- Dame un resumen de mis actividades.
- ¿Cuántas tareas tengo completadas?
- ¿Cuántos proyectos y ejercicios tengo registrados?
- Muéstrame mi progreso por estados de tareas.

## Endpoint

GET https://breathecode.herokuapp.com/v1/assignment/user/me/task

Parámetros:

- limit=50
- offset para paginación

## Procedimiento

1. Consultar las tareas accesibles del estudiante.
2. Recuperar todas las páginas.
3. Ejecutar desde el workspace:

   python3 -B skills/4geeks-progress-summary/scripts/progress_summary.py

4. Interpretar el JSON obtenido.
5. Mostrar el total de tareas.
6. Agrupar por estado y por tipo.
7. Distinguir los estados reportados por la API.
8. Informar cualquier error de consulta.

## Autenticación

El script admite FOURGEEKS_STUDENT_TOKEN
cuando esté disponible en un entorno autorizado.

No asumir que el gestor de secretos de OpenClaw
inyecta automáticamente esta variable.

No pedir credenciales por Telegram.

## Output esperado

Respuesta breve en español con:

- Total de tareas accesibles.
- Cantidad por estado.
- Cantidad por tipo.
- Distribución de estados dentro de cada tipo.
- Aclaración sobre el alcance de las métricas.

## Interpretación

Este resultado NO es el porcentaje oficial
de avance académico del curso.

El endpoint de actividad /v1/activity/me
devolvió HTTP 403 durante las pruebas.

DONE no implica necesariamente APPROVED.

No inferir aprobación a partir de entregas realizadas.

## Restricciones

- Exclusivamente lectura.
- No modificar estados.
- No realizar entregas.
- No inventar porcentajes.
- No presentar consultas parciales como completas.
- No mostrar credenciales.
- Respetar AGENTS.md.

## Limitaciones

La ejecución técnica puede probarse desde SSH.

La prueba conversacional desde Telegram y el
acceso automático al secreto siguen pendientes
mientras LiteLLM permanezca sin presupuesto.
