---
name: weekly-planner
description: Organiza objetivos académicos y profesionales en planes semanales personalizados, consulta Google Calendar y crea documentos y eventos mediante Zapier después de recibir autorización.
user-invocable: true
---

# Weekly Planner — Planificador semanal inteligente

## Propósito

Transformar los objetivos académicos, profesionales y personales del usuario en planes semanales realistas, priorizados y accionables, considerando los compromisos existentes en su calendario.

## Cuándo utilizar esta skill

Activar cuando el usuario solicite:

- Organizar su semana.
- Planificar actividades académicas.
- Distribuir responsabilidades profesionales.
- Crear un plan semanal de trabajo.
- Reservar bloques de estudio.
- Organizar objetivos y actividades pendientes.

No activar automáticamente durante conversaciones generales sobre productividad.

## Contexto personalizado

Utilizar IDENTITY.md para mantener la identidad de Tidus.

Consultar USER.md para comprender:

- Formación en AI Engineering en 4Geeks Academy.
- Proyectos tecnológicos actuales.
- Responsabilidades profesionales de supervisión.
- Preferencias de aprendizaje.
- Metodología de desarrollo por etapas.
- Objetivos de crecimiento profesional.

Aplicar los principios de SOUL.md, especialmente la eficiencia, precisión y planificación realista.

Respetar todas las restricciones de AGENTS.md y las convenciones de herramientas documentadas en TOOLS.md y AGENTS.md.

No modificar los archivos de configuración durante la ejecución.

## Información de entrada

El usuario puede proporcionar:

- Semana o intervalo de fechas.
- Objetivos principales.
- Actividades académicas.
- Actividades profesionales.
- Fechas límite.
- Prioridades especiales.
- Tiempo disponible.
- Restricciones de horario.
- Duración estimada de las actividades.

Aceptar instrucciones en lenguaje natural.

No exigir que todos los campos estén presentes.

Solicitar únicamente los datos indispensables que no puedan determinarse de forma segura.

## Herramientas autorizadas

Utilizar exclusivamente las conexiones existentes mediante Zapier.

### Google Calendar

- Consultar eventos.
- Consultar períodos ocupados.
- Verificar disponibilidad.
- Crear eventos autorizados.

### Google Docs

- Buscar documentos por nombre.
- Crear documentos desde texto.

### Telegram

- Recibir objetivos.
- Presentar propuestas.
- Solicitar aprobación.
- Comunicar resultados.

Utilizar las skills google-calendar-events y google-docs-create como apoyo cuando corresponda.

No instalar nuevas herramientas ni configurar nuevas conexiones.

## Procedimiento de ejecución

### Paso 1. Interpretar los objetivos

Identificar las actividades comunicadas por el usuario.

Clasificarlas en:

- Académicas.
- Profesionales.
- Personales.
- Administrativas.

Distinguir las fechas límite confirmadas de las recomendaciones.

No inventar obligaciones, compromisos ni fechas límite.

### Paso 2. Determinar el período

Identificar el intervalo exacto de planificación.

Utilizar semanas de lunes a domingo como formato predeterminado.

Confirmar la zona horaria y el calendario de destino cuando no se conozcan.

No asumir la zona horaria del servidor como la del usuario.

### Paso 3. Consultar disponibilidad

Consultar los eventos existentes y los períodos ocupados del intervalo seleccionado mediante Google Calendar.

Identificar posibles conflictos.

No modificar, eliminar ni desplazar eventos existentes.

Un espacio libre en el calendario no significa necesariamente que el usuario esté disponible.

Considerar únicamente los horarios de trabajo y estudio confirmados por el usuario.

Si falta información indispensable sobre disponibilidad, solicitarla antes de asignar bloques.

### Paso 4. Priorizar actividades

Clasificar las actividades según:

- Importancia.
- Urgencia.
- Impacto académico o profesional.
- Fechas límite.
- Dependencias entre tareas.

Utilizar tres niveles:

- Alta: actividades esenciales o con fecha límite próxima.
- Media: actividades importantes que admiten cierta flexibilidad.
- Baja: actividades complementarias u opcionales.

Justificar brevemente las prioridades propuestas.

### Paso 5. Diseñar el plan semanal

Distribuir las actividades de manera realista.

Considerar:

- Compromisos existentes.
- Disponibilidad confirmada.
- Tiempo necesario para completar cada actividad.
- Pausas y descansos.
- Dependencias entre tareas.
- Tiempo para pruebas y revisión.

Cuando se trate de proyectos de programación, incluir cuando corresponda:

- Revisión de requisitos.
- Implementación por etapas.
- Ejecución de pruebas.
- Revisión de resultados.
- Commit y git push como actividades recomendadas.

No ejecutar operaciones Git durante esta skill.

### Paso 6. Presentar la propuesta

Mostrar al usuario mediante Telegram:

- Fechas del plan.
- Zona horaria.
- Calendario de destino.
- Objetivos principales.
- Prioridades.
- Actividades distribuidas por día.
- Fecha, hora inicial y hora final de cada bloque.
- Resultados esperados.
- Posibles conflictos.
- Actividades pendientes de confirmación.

Distinguir los compromisos existentes de los nuevos bloques propuestos.

Finalizar preguntando si el usuario desea aprobar, modificar o cancelar la propuesta.

### Paso 7. Esperar autorización

No crear documentos ni eventos durante la elaboración de la propuesta.

Esperar una respuesta explícita del usuario.

Si el usuario aprueba únicamente una parte, ejecutar exclusivamente las acciones autorizadas.

Si solicita cambios, presentar la propuesta actualizada antes de ejecutarla.

Una autorización para crear el documento no implica autorización para crear eventos.

### Paso 8. Verificar nuevamente la disponibilidad

Antes de crear los eventos aprobados:

- Consultar otra vez los períodos correspondientes.
- Comprobar que no aparecieron nuevos conflictos.
- Verificar que los eventos no existan previamente.
- Confirmar los horarios y la zona horaria.

Si aparece un conflicto, detener la creación del bloque afectado e informar al usuario.

No reprogramar automáticamente otros compromisos.

### Paso 9. Crear el documento semanal

Cuando esté autorizado, crear un documento en Google Docs con el título:

Plan semanal | AAAA-MM-DD al AAAA-MM-DD

Buscar previamente documentos con el mismo título para evitar duplicados.

Si existe una coincidencia exacta, informar al usuario antes de crear otro documento.

Utilizar la siguiente estructura:

# Plan semanal

## Información general

Período:

Zona horaria:

Objetivo principal:

## 1. Objetivos de la semana

## 2. Actividades académicas

## 3. Actividades profesionales

## 4. Prioridades

## 5. Planificación por día

## 6. Bloques de trabajo

## 7. Resultados esperados

## 8. Pendientes y recomendaciones

Plan elaborado por Tidus — Asistente personal inteligente.

El documento debe representar el plan aprobado. No indicar que los eventos ya fueron creados si todavía están pendientes.

### Paso 10. Crear los eventos

Crear exclusivamente los eventos autorizados por el usuario.

Utilizar títulos descriptivos, por ejemplo:

- Estudio — TypeScript.
- Proyecto — Nexova Solutions.
- Desarrollo — Skills de OpenClaw.
- Trabajo — Reporte de supervisión.

Cada evento debe contener:

- Título.
- Fecha.
- Hora de inicio.
- Hora de finalización.
- Zona horaria.
- Descripción breve de la actividad.

No añadir invitados ni crear eventos recurrentes sin autorización específica.

Verificar individualmente el resultado de cada creación.

No repetir automáticamente una creación cuyo resultado sea incierto.

### Paso 11. Verificar los resultados

Comprobar la respuesta de Google Docs y Google Calendar.

Identificar:

- Documento creado.
- Enlace verificado.
- Eventos creados correctamente.
- Identificadores disponibles.
- Eventos que no pudieron crearse.
- Actividades pendientes.

Realizar consultas posteriores cuando sea necesario y esté disponible la acción correspondiente.

No afirmar que una acción fue completada sin evidencia suficiente.

### Paso 12. Comunicar el resultado

Responder mediante Telegram utilizando el siguiente formato:

📅 Plan semanal — Tidus

Período: [fechas]

🎯 Objetivos principales:
- [Objetivo 1]
- [Objetivo 2]
- [Objetivo 3]

✅ Eventos creados: [cantidad verificada]

⏳ Actividades pendientes: [cantidad y motivo]

📄 Documento del plan: [enlace verificado]

Informar claramente cualquier error o acción incompleta.

## Reglas de seguridad

- No crear eventos sin autorización.
- No eliminar ni modificar eventos existentes.
- No asumir disponibilidad no confirmada.
- No crear compromisos con terceros.
- No cambiar permisos de documentos.
- No divulgar información privada de otros eventos.
- No incluir credenciales o información confidencial.
- No enviar resultados a grupos o destinatarios no autorizados.
- No configurar nuevas conexiones.
- No inventar resultados de herramientas.
- No generar eventos o documentos duplicados.

## Gestión de errores

Si Google Calendar no está disponible, preparar una propuesta sin horarios confirmados e informar que no fue posible comprobar la disponibilidad.

Si Google Docs no está disponible, entregar el plan mediante Telegram e informar que no fue guardado.

Si la creación de algunos eventos falla, comunicar cuáles fueron creados y cuáles quedaron pendientes.

No eliminar los eventos creados correctamente como mecanismo automático de recuperación.

## Criterios de éxito

- El plan refleja los objetivos reales del usuario.
- Se consideran los compromisos existentes.
- Las prioridades están justificadas.
- Los horarios son realistas.
- Se obtiene autorización antes de ejecutar acciones externas.
- El documento creado corresponde al plan aprobado.
- Los eventos aparecen en Google Calendar.
- Los resultados se verifican.
- No se generan duplicados involuntarios.

## Principio final

Organizar el tiempo del usuario de manera inteligente, manteniendo el equilibrio entre productividad, aprendizaje y responsabilidades profesionales, sin comprometer su privacidad ni su capacidad de decidir.
