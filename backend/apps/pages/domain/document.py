"""Operaciones sobre el documento de página. Sin dependencias de Django."""

import copy
from typing import Any

import jsonpatch
from jsonschema import Draft202012Validator

from .errors import InvalidDocument, InvalidPatch

Document = dict[str, Any]


def apply_patch(document: Document, operations: list[dict]) -> Document:
    """Aplica operaciones JSON Patch y devuelve un documento nuevo."""
    try:
        return jsonpatch.apply_patch(copy.deepcopy(document), operations)
    except (jsonpatch.JsonPatchException, jsonpatch.JsonPointerException) as exc:
        raise InvalidPatch(str(exc)) from exc


def validate(document: Document, schema: dict) -> None:
    """Valida el documento contra el JSON Schema generado desde la librería de secciones."""
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(document), key=lambda e: list(e.path))
    if errors:
        raise InvalidDocument(
            [f"/{'/'.join(str(p) for p in e.path)}: {e.message}" for e in errors]
        )


def empty_document(*, library_version: str, locale: str = "es") -> Document:
    return {
        "library": library_version,
        "locale": locale,
        "theme": {"palette": "default", "font": "default", "radius": "md"},
        "sections": [],
    }
