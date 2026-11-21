#!/usr/bin/env python3
"""Comprueba la autenticación con BreatheCode sin mostrar credenciales."""

import getpass
import json
import os
import sys
import urllib.error
import urllib.request

URL = "https://breathecode.herokuapp.com/v1/admissions/user/me"


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def main():
    token = os.environ.get("FOURGEEKS_STUDENT_TOKEN")

    if not token:
        if not sys.stdin.isatty():
            print(json.dumps({
                "ok": False,
                "error": "Credencial no disponible en este entorno"
            }, ensure_ascii=False))
            return 2

        token = getpass.getpass("Token 4Geeks (oculto): ")

    if not token.strip():
        print('{"ok": false, "error": "Token vacío"}')
        return 2

    request = urllib.request.Request(
        URL,
        headers={
            "Authorization": f"Token {token.strip()}",
            "Accept": "application/json",
        },
        method="GET",
    )

    opener = urllib.request.build_opener(NoRedirect)

    try:
        with opener.open(request, timeout=20) as response:
            data = json.load(response)

            if not isinstance(data, dict):
                print('{"ok": false, "error": "Respuesta inesperada"}')
                return 1

            academies = data.get("profile_academy")
            count = len(academies) if isinstance(academies, list) else None

            print(json.dumps({
                "ok": True,
                "http_status": response.status,
                "autenticacion": "exitosa",
                "academias_reportadas": count,
            }, ensure_ascii=False))
            return 0

    except urllib.error.HTTPError as error:
        print(json.dumps({
            "ok": False,
            "http_status": error.code,
            "error": "La API rechazó la solicitud",
        }, ensure_ascii=False))
        return 1

    except (urllib.error.URLError, TimeoutError):
        print('{"ok": false, "error": "No fue posible conectar"}')
        return 1

    except (ValueError, TypeError):
        print('{"ok": false, "error": "Respuesta JSON no válida"}')
        return 1


if __name__ == "__main__":
    sys.exit(main())
