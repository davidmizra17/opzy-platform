import json
from pathlib import Path

import pytest

from apps.pages.domain import document as doc
from apps.pages.domain.errors import InvalidDocument, InvalidPatch
from apps.pages.domain.facts import find_unsupported_claims

SCHEMA = json.loads(
    (Path(__file__).resolve().parent.parent / "schema" / "page-document.schema.json").read_text()
)


def test_empty_document_is_valid():
    doc.validate(doc.empty_document(library_version="0.1.0"), SCHEMA)


def test_patch_returns_new_document():
    original = doc.empty_document(library_version="0.1.0")
    updated = doc.apply_patch(original, [{"op": "replace", "path": "/theme/radius", "value": "lg"}])
    assert updated["theme"]["radius"] == "lg"
    assert original["theme"]["radius"] == "md"


def test_invalid_patch_raises():
    with pytest.raises(InvalidPatch):
        doc.apply_patch({}, [{"op": "remove", "path": "/missing"}])


def test_schema_violation_raises():
    bad = doc.empty_document(library_version="0.1.0") | {"locale": "fr"}
    with pytest.raises(InvalidDocument):
        doc.validate(bad, SCHEMA)


def test_facts_rule_flags_invented_numbers():
    document = {"sections": [{"props": {"hours": "Abierto de 7:00 a 19:00", "price": "USD 25"}}]}
    assert find_unsupported_claims(document, ["Abrimos 7:00 a 19:00"]) == ["25"]
