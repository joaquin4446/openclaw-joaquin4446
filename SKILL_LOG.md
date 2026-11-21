
# SKILL_LOG — Integración OpenClaw con 4Geeks

## Objetivo

Crear seis skills especializadas para consultar información
académica de mi cuenta de 4Geeks mediante la API BreatheCode.

## Entorno

- Agente: Tidus
- Plataforma: OpenClaw 2026.10.9
- Interfaz: Telegram
- Integración: API BreatheCode
- Lenguaje principal de documentación: español

## Conversación de descubrimiento

### Solicitud inicial

Pedí a Tidus que me ayudara a integrar mi cuenta de estudiante
de 4Geeks mediante un token seguro y construir las skills
conversacionalmente.

### Resultado

OpenClaw rechazó la solicitud porque se agotó el presupuesto
de LiteLLM asignado por 4Geeks Academy.

Error: LLM request rejected: Budget has been exceeded.

### Decisión

Continuar mediante implementación asistida externamente,
pruebas de API desde la terminal y documentación transparente.

Las pruebas desde la terminal no se presentarán como ejecuciones
conversacionales de OpenClaw.

## Skills requeridas

### Skill 1 — Autenticación

**Nombre:** `4geeks-authenticate`

**Estado:** Implementada y validada mediante terminal. Ejecución conversacional pendiente.

**Necesidad:** Comprobar que el token de estudiante permite acceder a BreatheCode antes de consultar información académica.

**Solicitud que originó la skill:** Enseñar a Tidus a conectarse de forma segura a mi cuenta de 4Geeks y comprobar que la autenticación funciona.

**Método de construcción:** La conversación inicial con Tidus fue interrumpida por el límite de presupuesto de LiteLLM. Se continuó mediante desarrollo asistido externamente y pruebas reales desde la terminal, sin atribuirle a Tidus acciones que no ejecutó.

**Endpoint:** `GET /v1/admissions/user/me`

**Input:** Token de estudiante, introducido mediante entrada oculta en las pruebas manuales. También se registró `FOURGEEKS_STUDENT_TOKEN` en el gestor de secretos de OpenClaw. Su acceso automático desde la skill sigue pendiente de comprobación.

**Output:** Resultado JSON breve con el estado de autenticación, código HTTP y cantidad de academias cuando esté disponible.

**¿Por qué este input?** Porque la API requiere una credencial para identificar al estudiante. El usuario no debería tener que introducirla en cada conversación.

**¿Por qué este output?** Porque permite comprobar fácilmente si existe acceso sin mostrar datos personales ni credenciales.

**Archivos implementados:**
- `skills/4geeks-authenticate/SKILL.md`
- `skills/4geeks-authenticate/scripts/check_auth.py`

**Prueba realizada:** Ejecución de `check_auth.py` desde el VPS y consulta real a BreatheCode.

**Resultado obtenido:**
- HTTP 200.
- `ok: true`.
- Autenticación exitosa.
- `academias_reportadas: null`, porque la respuesta no contenía ese campo como una lista.

**Problema encontrado:** OpenClaw inicialmente no reconocía la skill. Se corrigió el inicio del archivo `SKILL.md` y se repitió la comprobación.

**Verificación final:** `openclaw skills check` mostró 62 skills instaladas, 27 disponibles y `4geeks-authenticate` reconocida.

**Limitación:** No se ha probado la ejecución desde Telegram debido al presupuesto agotado del modelo de IA. Tampoco se ha verificado todavía la inyección automática del secreto protegido.

**Conclusión:** La autenticación mediante la API y el reconocimiento nativo de la skill funcionan. La integración conversacional completa permanece pendiente.

### Skill 2 — Mis proyectos

- Nombre: pendiente de definir
- Prompt de diseño: pendiente
- Responsabilidad: consultar proyectos asignados y estados
- Endpoint: pendiente de verificar
- Prueba: pendiente
- Resultado: pendiente
- Estado: sin implementar

### Skill 3 — Trabajo pendiente

- Nombre: pendiente de definir
- Prompt de diseño: pendiente
- Responsabilidad: identificar entregas pendientes
- Endpoint: pendiente de verificar
- Prueba: pendiente
- Resultado: pendiente
- Estado: sin implementar

### Skill 4 — Resumen de progreso

- Nombre: pendiente de definir
- Prompt de diseño: pendiente
- Responsabilidad: resumir el progreso académico
- Endpoint: pendiente de verificar
- Prueba: pendiente
- Resultado: pendiente
- Estado: sin implementar

### Skill 5 — Capacidad adicional

- Nombre: pendiente
- Necesidad identificada: pendiente
- Prompt de diseño: pendiente
- Endpoint: pendiente de verificar
- Prueba: pendiente
- Resultado: pendiente
- Estado: sin implementar

### Skill 6 — Capacidad adicional

- Nombre: pendiente
- Necesidad identificada: pendiente
- Prompt de diseño: pendiente
- Endpoint: pendiente de verificar
- Prueba: pendiente
- Resultado: pendiente
- Estado: sin implementar

## Seguridad

El token de estudiante no se almacenará en este documento,
en las skills ni en el repositorio.

Se utilizará un mecanismo protegido y compatible con
OpenClaw para acceder a la credencial.

## Evidencias

Las pruebas se documentarán con:
- Comando o solicitud ejecutada.
- Endpoint real utilizado.
- Código de respuesta HTTP.
- Resumen del resultado, sin información confidencial.
- Estado de la prueba.

## Limitaciones pendientes

- Presupuesto del modelo de OpenClaw agotado.
- Pruebas conversacionales desde Telegram no disponibles.

---

## Validación técnica — Skill 2: 4geeks-projects

**Nombre:** `4geeks-projects`

**Estado:** Implementada y validada desde la terminal.
Prueba conversacional pendiente por límite de LiteLLM.

**Necesidad:** Consultar los proyectos académicos del estudiante
y conocer sus estados sin acceder manualmente a la plataforma.

**Endpoint:**
GET /v1/assignment/user/me/task

**Parámetros:** task_type=PROJECT, limit y offset.

**Input:** Token de estudiante, proporcionado mediante entrada
oculta durante la prueba. El script también admite una variable
de entorno segura, cuya integración automática con el gestor
de secretos de OpenClaw sigue pendiente de verificación.

**Output:** JSON con total_proyectos, por_estado y,
opcionalmente, los proyectos y sus estados individuales.

**Archivos:**
- skills/4geeks-projects/SKILL.md
- skills/4geeks-projects/scripts/list_projects.py

**Diseño:** Recuperación paginada, comprobación de registros
duplicados, validación del total y agrupación por estado.

**Prueba real ejecutada:**
python3 -B skills/4geeks-projects/scripts/list_projects.py --summary

**Resultados:**
- Consulta completada correctamente.
- Total de proyectos: 21.
- DONE: 20.
- PENDING: 1.
- La cantidad coincide con el total previamente reportado
  por BreatheCode.

**Reconocimiento por OpenClaw:**
- openclaw skills info 4geeks-projects: Ready.
- Skills totales: 63.
- Skills elegibles: 28.
- Visible para el modelo: sí.
- Disponible como comando: sí.

**Interpretación:** DONE es el estado devuelto por la API.
No se considera equivalente a APPROVED. La distribución
tampoco representa el porcentaje oficial de avance del curso.

**Limitaciones:** No se ha probado la ejecución desde Telegram
ni el acceso automático al secreto protegido de OpenClaw.

**Conclusión:** Skill implementada, reconocida por OpenClaw
y validada técnicamente con datos reales de BreatheCode.
