#!/usr/bin/env python3
"""Consulta una página de eventos próximos de BreatheCode."""

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
ENDPOINT = "/v1/events/all"
LIMIT = 50


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def consultar_eventos(token, academy_id=None):
    params = {
        "upcoming": "true",
        "limit": LIMIT,
    }

    if academy_id is not None:
        params["academy"] = academy_id

    url = BASE + ENDPOINT + "?" + urllib.parse.urlencode(params)

    request = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Token {token}",
            "Accept": "application/json",
        },
        method="GET",
    )

    opener = urllib.request.build_opener(NoRedirect)

    with opener.open(request, timeout=20) as response:
        data = json.load(response)

    if not isinstance(data, list):
        raise ValueError("La API no devolvió una lista")

    if len(data) > LIMIT:
        raise ValueError("La API excedió el límite solicitado")

    eventos = []
    vistos = set()

    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Registro de evento inválido")

        event_id = item.get("id")

        if type(event_id) is not int or event_id in vistos:
            raise ValueError("ID inválido o repetido")

        vistos.add(event_id)

        academia = item.get("academy")
        if not isinstance(academia, dict):
            academia = {}

        if academy_id is not None:
            if academia.get("id") != academy_id:
                raise ValueError("Evento de otra academia")

        tipo = item.get("event_type")
        if not isinstance(tipo, dict):
            tipo = {}

        eventos.append({
            "id": event_id,
            "titulo": item.get("title"),
            "inicio": item.get("starting_at"),
            "fin": item.get("ending_at"),
            "tipo": tipo.get("name"),
            "academia": academia.get("name"),
            "academia_id": academia.get("id"),
            "en_linea": item.get("online_event"),
            "estado": item.get("status"),
            "url": item.get("url"),
        })

    return eventos


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--academy", type=int)

    args = parser.parse_args()

    if args.academy is not None and args.academy <= 0:
        parser.error("--academy debe ser positivo")

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
        eventos = consultar_eventos(token, args.academy)

        por_academia = Counter(
            evento["academia"] or "SIN_ACADEMIA"
            for evento in eventos
        )

        resultado = {
            "ok": True,
            "fuente": "BreatheCode Events API",
            "eventos_en_respuesta": len(eventos),
            "limite_solicitado": LIMIT,
            "total_global": None,
            "paginacion": "no_verificada",
            "alcance": (
                "academia_filtrada"
                if args.academy is not None
                else "eventos_generales"
            ),
            "por_academia": dict(
                sorted(por_academia.items())
            ),
            "advertencia": (
                "La lista puede ser parcial. "
                "No se conoce el total global de eventos. "
                "Sin academia confirmada, no se puede "
                "asegurar que correspondan al estudiante."
            ),
        }

        if not args.summary:
            eventos.sort(
                key=lambda x: str(x["inicio"] or "")
            )

            resultado["eventos"] = eventos[:20]
            resultado["eventos_mostrados"] = min(
                len(eventos), 20
            )

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
        }))
        return 1

    except (urllib.error.URLError, TimeoutError):
        print('{"ok": false, "error": "Error de conexión"}')
        return 1

    except (ValueError, TypeError):
        print('{"ok": false, "error": "Respuesta inválida"}')
        return 1


if __name__ == "__main__":
    sys.exit(main())
