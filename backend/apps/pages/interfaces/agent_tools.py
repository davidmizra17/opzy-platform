"""Herramientas que el agente puede llamar sobre la página.

El agente nunca escribe HTML: describe cambios al documento con JSON Patch.
"""

UPDATE_PAGE_TOOL = {
    "name": "update_page",
    "description": (
        "Cambia la página del cliente aplicando operaciones JSON Patch (RFC 6902) al documento. "
        "Solo usa tipos de sección, campos y variantes del catálogo. Escribe textos solo con datos "
        "que el cliente dio; si falta un dato, deja el campo vacío para que se muestre un "
        "placeholder. Si la llamada falla, lee el error y corrige las operaciones."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "base_version": {
                "type": "integer",
                "description": "Versión del documento sobre la que aplicas los cambios.",
            },
            "operations": {
                "type": "array",
                "minItems": 1,
                "maxItems": 50,
                "items": {
                    "type": "object",
                    "properties": {
                        "op": {"enum": ["add", "remove", "replace", "move", "copy"]},
                        "path": {"type": "string"},
                        "from": {"type": "string"},
                        "value": {},
                    },
                    "required": ["op", "path"],
                },
            },
            "summary": {
                "type": "string",
                "description": "Una frase para el cliente sobre lo que cambiaste.",
            },
        },
        "required": ["base_version", "operations", "summary"],
    },
}
