import uuid

import pytest

from apps.pages.domain.errors import UnsupportedClaims
from apps.pages.infrastructure.repository import VersionConflict, page_use_cases


@pytest.mark.django_db
def test_update_creates_new_version_and_revert_restores():
    uc = page_use_cases()
    page = uc.create_page(visitor_id=uuid.uuid4(), conversation_id=None)
    v2 = uc.update_page(
        page.page_id,
        operations=[{"op": "replace", "path": "/theme/radius", "value": "lg"}],
        base_version=1,
        client_facts=[],
    )
    assert v2.version == 2 and v2.document["theme"]["radius"] == "lg"
    v3 = uc.revert_page(page.page_id, to_version=1, base_version=2)
    assert v3.version == 3 and v3.document["theme"]["radius"] == "md"


@pytest.mark.django_db
def test_stale_base_version_conflicts():
    uc = page_use_cases()
    page = uc.create_page(visitor_id=uuid.uuid4(), conversation_id=None)
    op = [{"op": "replace", "path": "/theme/radius", "value": "sm"}]
    uc.update_page(page.page_id, operations=op, base_version=1, client_facts=[])
    with pytest.raises(VersionConflict):
        uc.update_page(page.page_id, operations=op, base_version=1, client_facts=[])


@pytest.mark.django_db
def test_invented_facts_are_rejected():
    uc = page_use_cases()
    page = uc.create_page(visitor_id=uuid.uuid4(), conversation_id=None)
    hero = {
        "id": "hero",
        "type": "hero-split",
        "props": {
            "variant": "image-right",
            "headline": "Panadería Sol, desde 1998",
            "cta": {"label": "Pedir", "action": "whatsapp"},
        },
    }
    op = [{"op": "add", "path": "/sections/-", "value": hero}]
    with pytest.raises(UnsupportedClaims):
        uc.update_page(page.page_id, operations=op, base_version=1, client_facts=[])
