"""Regla de hechos: el agente solo escribe datos que el cliente dio.

Primera versión, deliberadamente simple: detecta números (precios, horarios, años,
porcentajes, teléfonos) en el texto de la página que no aparecen en los hechos del cliente.
"""

import re
from collections.abc import Iterable

NUMBER = re.compile(r"\d+(?:[.,:]\d+)*")


def _strings(value) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from _strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from _strings(v)


def find_unsupported_claims(document: dict, client_facts: Iterable[str]) -> list[str]:
    known = {n for fact in client_facts for n in NUMBER.findall(fact)}
    found = {
        n for text in _strings(document.get("sections", [])) for n in NUMBER.findall(text)
    }
    return sorted(found - known)
