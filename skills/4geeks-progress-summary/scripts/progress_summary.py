#!/usr/bin/env python3
"""Resumen de tareas académicas accesibles en BreatheCode."""

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


def recuperar_tareas(token):
    opener = urllib.request.build_opener(NoRedirect)

    tareas = []
    ids = set()
    offset = 0
    total = None

    for _ in range(MAX_PAGES):
        params = urllib.parse.urlencode({
            "limit": PAGE_SIZE,
            "offset": offset,
        })

        url = BASE + ENDPOINT + "?" + params

        request = urllib.request.Request(
            url,
            headers={
                "Authorization": f"Token {token}",
                "Accept": "application/json",
            },
            method="GET",
        )

        with opener.open(request, timeout=20) as response:
            data = json.load(response)

        if not isinstance(data, dict):
            raise ValueError("Formato inesperado")

        results = data.get("results")
        count = data.get("count")

        if not isinstance(results, list):
            raise ValueError("No se encontró results")

        if type(count) is not int or count < 0:
            raise ValueError("Count inválido")

        if total is None:
            total = count
        elif total != count:
            raise ValueError(
                "El total cambió durante la consulta"
            )

        for item in results:
            if not isinstance(item, dict):
                raise ValueError("Registro inválido")

            task_id = item.get("id")

            if task_id is None or task_id in ids:
                raise ValueError(
                    "Identificador ausente o duplicado"
                )

            ids.add(task_id)

            tareas.append({
                "tipo": item.get("task_type") or "SIN_TIPO",
                "estado": item.get("task_status") or "SIN_ESTADO",
            })

        if len(tareas) == total:
            return tareas

        if len(tareas) > total:
            raise ValueError(
                "Se recibieron más registros que el total"
            )

        if not results or not data.get("next"):
            raise ValueError("Paginación incompleta")

        offset += len(results)

    raise ValueError("Límite de páginas alcanzado")


def main():
    token = os.environ.get(
        "FOURGEEKS_STUDENT_TOKEN", ""
    ).strip()

    if not token:
        if not sys.stdin.isatty():
            print(json.dumps({
                "ok": False,
                "error": "Credencial no disponible",
            }))
            return 2

        token = getpass.getpass(
            "Token 4Geeks (oculto): "
        ).strip()

    if not token:
        print('{"ok": false, "error": "Token vacío"}')
        return 2

    try:
        tareas = recuperar_tareas(token)

        por_estado = Counter()
        por_tipo = Counter()
        matriz = {}

        for tarea in tareas:
            tipo = tarea["tipo"]
            estado = tarea["estado"]

            if not isinstance(tipo, str):
                tipo = "SIN_TIPO"

            if not isinstance(estado, str):
                estado = "SIN_ESTADO"

            por_estado[estado] += 1
            por_tipo[tipo] += 1

            if tipo not in matriz:
                matriz[tipo] = Counter()

            matriz[tipo][estado] += 1

        resultado = {
            "ok": True,
            "fuente": "BreatheCode Assignment API",
            "total_tareas": len(tareas),
            "por_estado": dict(sorted(por_estado.items())),
            "por_tipo": dict(sorted(por_tipo.items())),
            "detalle_por_tipo": {
                tipo: dict(sorted(estados.items()))
                for tipo, estados in sorted(matriz.items())
            },
            "advertencia": (
                "Resumen de estados de tareas accesibles. "
                "No equivale al progreso oficial del curso. "
                "DONE no significa necesariamente APPROVED."
            ),
        }

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
        print(
            '{"ok": false, "error": "Error de conexión"}'
        )
        return 1

    except (ValueError, TypeError):
        print(
            '{"ok": false, "error": "Respuesta incompleta o inválida"}'
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
