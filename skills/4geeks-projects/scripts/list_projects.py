#!/usr/bin/env python3
"""Consulta los proyectos de 4Geeks con paginación segura."""

import argparse
import getpass
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter

BASE = "https://breathecode.herokuapp.com"
ENDPOINT = "/v1/assignment/user/me/task"
PAGE_SIZE = 50
MAX_PAGES = 100


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def consultar(token):
    opener = urllib.request.build_opener(NoRedirect)
    proyectos = []
    identificadores = set()
    offset = 0
    total = None

    for _ in range(MAX_PAGES):
        parametros = urllib.parse.urlencode({
            "task_type": "PROJECT",
            "limit": PAGE_SIZE,
            "offset": offset,
        })

        url = BASE + ENDPOINT + "?" + parametros

        solicitud = urllib.request.Request(
            url,
            headers={
                "Authorization": f"Token {token}",
                "Accept": "application/json",
            },
            method="GET",
        )

        with opener.open(solicitud, timeout=20) as respuesta:
            datos = json.load(respuesta)

        if not isinstance(datos, dict):
            raise ValueError("Formato de respuesta inesperado")

        registros = datos.get("results")
        cantidad = datos.get("count")

        if not isinstance(registros, list):
            raise ValueError("La respuesta no contiene results")

        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La respuesta no contiene un count válido")

        if total is None:
            total = cantidad
        elif cantidad != total:
            raise ValueError("El total cambió durante la consulta")

        if not registros and len(proyectos) < total:
            raise ValueError("Página vacía antes de completar resultados")

        for registro in registros:
            if not isinstance(registro, dict):
                raise ValueError("Registro de proyecto inesperado")

            if registro.get("task_type") != "PROJECT":
                raise ValueError("La API devolvió una tarea no PROJECT")

            identificador = registro.get("id")

            if identificador in identificadores:
                raise ValueError("La paginación devolvió un proyecto repetido")

            identificadores.add(identificador)

            proyectos.append({
                "id": identificador,
                "titulo": registro.get("title"),
                "estado": registro.get("task_status"),
                "revision": registro.get("revision_status"),
                "entregado_el": registro.get("delivered_at"),
            })

        if len(proyectos) >= total:
            if len(proyectos) != total:
                raise ValueError("Cantidad de resultados inconsistente")
            return proyectos

        if not datos.get("next"):
            raise ValueError("Paginación incompleta: falta next")

        offset += len(registros)

    raise ValueError("Se superó el límite de páginas")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Mostrar únicamente las cantidades por estado",
    )
    args = parser.parse_args()

    token = os.environ.get("FOURGEEKS_STUDENT_TOKEN", "").strip()

    if not token:
        if not sys.stdin.isatty():
            print(json.dumps({
                "ok": False,
                "error": "Credencial no disponible",
            }))
            return 2

        token = getpass.getpass("Token 4Geeks (oculto): ").strip()

    if not token:
        print('{"ok": false, "error": "Token vacío"}')
        return 2

    try:
        proyectos = consultar(token)
        resumen = dict(sorted(Counter(
            proyecto["estado"] or "SIN_ESTADO"
            for proyecto in proyectos
        ).items()))

        resultado = {
            "ok": True,
            "total_proyectos": len(proyectos),
            "por_estado": resumen,
        }

        if not args.summary:
            resultado["proyectos"] = proyectos

        print(json.dumps(
            resultado,
            ensure_ascii=False,
            indent=2,
        ))
        return 0

    except urllib.error.HTTPError as error:
        print(json.dumps({
            "ok": False,
            "http_status": error.code,
            "error": "La API rechazó la consulta",
        }, ensure_ascii=False))
        return 1

    except (urllib.error.URLError, TimeoutError):
        print('{"ok": false, "error": "Error de conexión"}')
        return 1

    except (ValueError, TypeError):
        print('{"ok": false, "error": "Respuesta incompleta o inválida"}')
        return 1


if __name__ == "__main__":
    sys.exit(main())
