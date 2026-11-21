---
name: 4geeks-authenticate
description: Verifica de forma segura si el usuario puede autenticarse en la API de estudiantes de 4Geeks Academy.
user-invocable: true
---

# 4Geeks Authenticate

## Objetivo

Comprobar que la cuenta de estudiante puede acceder
correctamente a la API BreatheCode.

## Cuándo utilizar

Cuando el usuario pregunte:

- ¿Estoy conectado a 4Geeks?
- ¿Funciona mi token de estudiante?
- Verifica mi conexión con BreatheCode.

## API utilizada

GET https://breathecode.herokuapp.com/v1/admissions/user/me

## Autenticación

La credencial se identifica como FOURGEEKS_STUDENT_TOKEN.

No solicitar el token en Telegram ni mostrar su valor.

En ejecuciones administradas por OpenClaw, utilizar el
secreto proporcionado mediante el proxy de salida protegido.

El proxy debe estar configurado antes de ejecutar la skill
desde el agente. No asumir que está habilitado.

## Procedimiento

1. Comprobar que existe un entorno autorizado para la consulta.
2. Ejecutar desde el workspace:

   python3 -B skills/4geeks-authenticate/scripts/check_auth.py

3. Interpretar el resultado JSON.
4. Si HTTP es 200 y ok es true, informar que la
   autenticación funcionó.
5. Si HTTP es 401, informar que la autenticación falló.
6. Si HTTP es 403, informar que el acceso fue denegado.
7. No confundir autenticación con permisos sobre otros endpoints.
8. No interpretar cero academias reportadas como prueba
   definitiva de que no existen inscripciones.

## Output esperado

Un mensaje breve en español:

- Estado de autenticación.
- Resultado de la consulta.
- Advertencias relevantes.
- Próximo paso recomendado.

No mostrar nombre, correo, identificadores ni credenciales.

## Restricciones

- Skill exclusivamente de lectura.
- No modificar la cuenta.
- No instalar dependencias.
- No guardar respuestas privadas en Git.
- No inventar resultados.
- No acceder a otros endpoints.
- Respetar AGENTS.md y las reglas de seguridad de Tidus.

## Prueba

La skill se considera validada técnicamente cuando
el script consulta el endpoint y devuelve un resultado
coherente con el código HTTP recibido.

La prueba desde Telegram requiere que vuelva a estar
disponible el modelo de OpenClaw.
