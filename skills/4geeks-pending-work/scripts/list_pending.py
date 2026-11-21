#!/usr/bin/env python3
"""Consulta tareas pendientes o rechazadas en BreatheCode."""

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
STATES = ("PENDING", "REJECTED")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def get_tasks(token, state):
    opener = urllib.request.build_opener(NoRedirect)

    tasks = []
    ids = set()
    offset = 0
    expected = None

    for _ in range(MAX_PAGES):
        params = urllib.parse.urlencode({
            "task_status": state,
            "limit": PAGE_SIZE,
            "offset": offset,
        })

        request = urllib.request.Request(
            BASE + ENDPOINT + "?" + params,
            headers={
                "Authorization": f"Token {token}",
                "Accept": "application/json",
            },
            method="GET",
        )

        with opener.open(request, timeout=20) as response:
            data = json.load(response)

        if not isinstance(data, dict):
            raise ValueError("Respuesta inesperada")

        results = data.get("results")
        count = data.get("count")

        if not isinstance(results, list):
            raise ValueError("No se encontró results")

        if not isinstance(count, int) or count < 0:
            raise ValueError("Count inválido")

        if expected is None:
            expected = count
        elif expected != count:
            raise ValueError("El total cambió durante la consulta")

        for item in results:
            if not isinstance(item, dict):
                raise ValueError("Registro inválido")

            item_state = item.get("task_status")

            if item_state != state:
                raise ValueError(
                    "La API devolvió una tarea con estado inesperado"
                )

            task_id = item.get("id")

            if task_id is None or task_id in ids:
                raise ValueError(
                    "Identificador ausente o duplicado"
                )

            ids.add(task_id)

            tasks.append({
                "id": task_id,
                "titulo": item.get("title"),
                "tipo": item.get("task_type"),
                "estado": item_state,
                "revision": item.get("revision_status"),
            })

        if len(tasks) == expected:
            return tasks

        if len(tasks) > expected:
            raise ValueError("Resultados exceden el total")

        if not results or not data.get("next"):
            raise ValueError("Paginación incompleta")

        offset += len(results)

    raise ValueError("Límite de paginación alcanzado")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Mostrar solo cantidades, sin títulos",
    )
    args = parser.parse_args()

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
        pending = get_tasks(token, "PENDING")
        rejected = get_tasks(token, "REJECTED")

        all_tasks = pending + rejected

        ids = [task["id"] for task in all_tasks]

        if len(ids) != len(set(ids)):
            raise ValueError(
                "Una tarea aparece en varios estados"
            )

        by_type = dict(sorted(Counter(
            task["tipo"] or "SIN_TIPO"
            for task in all_tasks
        ).items()))

        result = {
            "ok": True,
            "pendientes": len(pending),
            "rechazadas": len(rejected),
            "total_requiere_atencion": len(all_tasks),
            "por_tipo": by_type,
        }

        if not args.summary:
            result["tareas"] = all_tasks

        print(json.dumps(
            result,
            ensure_ascii=False,
            indent=2,
        ))

        return 0

    except urllib.error.HTTPError as error:
        print(json.dumps({
            "ok": False,
            "http_status": error.code,
            "error": "La API rechazó una consulta",
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
