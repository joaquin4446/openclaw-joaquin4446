#!/usr/bin/env python3
"""Consulta recursos educativos de BreatheCode (solo lectura)."""

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
PATH = "/v1/registry/asset"
PAGE_SIZE = 50
MAX_PAGES = 100


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def tech_names(value):
    if isinstance(value, str):
        return [value]

    if not isinstance(value, list):
        return []

    names = []
    for item in value:
        if isinstance(item, str):
            names.append(item)
        elif isinstance(item, dict):
            name = (
                item.get("slug")
                or item.get("title")
                or item.get("name")
            )
            if isinstance(name, str):
                names.append(name)

    return names


def retrieve(token, asset_type):
    opener = urllib.request.build_opener(NoRedirect)

    collected = []
    seen_ids = set()
    expected = None
    offset = 0

    for _ in range(MAX_PAGES):
        params = urllib.parse.urlencode({
            "asset_type": asset_type,
            "limit": PAGE_SIZE,
            "offset": offset,
        })

        request = urllib.request.Request(
            BASE + PATH + "?" + params,
            headers={
                "Authorization": "Token " + token,
                "Accept": "application/json",
            },
            method="GET",
        )

        with opener.open(request, timeout=20) as response:
            data = json.load(response)

        if not isinstance(data, dict):
            raise ValueError("Respuesta no paginada")

        total = data.get("count")
        rows = data.get("results")

        if (
            type(total) is not int
            or total < 0
            or not isinstance(rows, list)
        ):
            raise ValueError("Count o results inválidos")

        if expected is None:
            expected = total
        elif expected != total:
            raise ValueError("El total cambió")

        if len(rows) > PAGE_SIZE:
            raise ValueError("Límite excedido")

        for row in rows:
            if not isinstance(row, dict):
                raise ValueError("Registro inválido")

            identifier = row.get("id")

            if (
                type(identifier) is not int
                or identifier in seen_ids
            ):
                raise ValueError("ID inválido o repetido")

            if row.get("asset_type") != asset_type:
                raise ValueError("Tipo de recurso inesperado")

            seen_ids.add(identifier)

            collected.append({
                "titulo": row.get("title"),
                "slug": row.get("slug"),
                "tipo": row.get("asset_type"),
                "dificultad": row.get("difficulty"),
                "idioma": row.get("lang"),
                "tecnologias": tech_names(
                    row.get("technologies")
                ),
                "estado_publicacion": row.get("status"),
            })

        if len(collected) == expected:
            return collected

        if (
            len(collected) > expected
            or not rows
            or not data.get("next")
        ):
            raise ValueError("Paginación incompleta")

        offset += len(rows)

    raise ValueError("Máximo de páginas alcanzado")


def main():
    parser = argparse.ArgumentParser(
        description="Buscar recursos educativos de 4Geeks"
    )

    parser.add_argument(
        "--type",
        choices=["EXERCISE", "LESSON", "PROJECT"],
        default="EXERCISE",
    )

    parser.add_argument(
        "--keyword",
        default="",
        help="Buscar en títulos, slugs y tecnologías",
    )

    parser.add_argument(
        "--summary",
        action="store_true",
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
        all_resources = retrieve(token, args.type)
        keyword = args.keyword.casefold().strip()

        matches = [
            item for item in all_resources
            if not keyword or keyword in " ".join([
                str(item["titulo"] or ""),
                str(item["slug"] or ""),
                " ".join(item["tecnologias"]),
            ]).casefold()
        ]

        by_difficulty = dict(sorted(Counter(
            str(item["dificultad"] or "NO_INDICADA")
            for item in matches
        ).items()))

        result = {
            "ok": True,
            "fuente": "BreatheCode Registry Asset API",
            "tipo_consultado": args.type,
            "recursos_recuperados": len(all_resources),
            "palabra_clave": args.keyword.strip() or None,
            "coincidencias": len(matches),
            "por_dificultad": by_difficulty,
            "alcance": "catalogo_educativo_no_personalizado",
        }

        if not args.summary:
            result["recursos"] = matches[:15]
            result["mostrados"] = min(len(matches), 15)
            result["hay_mas_coincidencias"] = len(matches) > 15

        print(json.dumps(
            result,
            ensure_ascii=False,
            indent=2,
        ))

        return 0

    except urllib.error.HTTPError as err:
        print(json.dumps({
            "ok": False,
            "http_status": err.code,
            "error": "Consulta rechazada",
        }, ensure_ascii=False))
        return 1

    except (urllib.error.URLError, TimeoutError):
        print('{"ok": false, "error": "Fallo de conexión"}')
        return 1

    except (ValueError, TypeError):
        print(
            '{"ok": false, "error": "Respuesta o paginación inválida"}'
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
