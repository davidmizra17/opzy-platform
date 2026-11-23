import json
from functools import cache
from pathlib import Path
from uuid import UUID

from django.db import transaction

from apps.pages.application.ports import PageSnapshot
from apps.pages.domain.errors import PageError
from apps.tracking import services as tracking

from .models import Page, PageVersion

SCHEMA_DIR = Path(__file__).resolve().parent.parent / "schema"


class VersionConflict(PageError):
    """Otra edición se guardó primero. El agente debe releer y reintentar."""


class DjangoPageRepository:
    def _snapshot(self, page: Page, version: PageVersion) -> PageSnapshot:
        return PageSnapshot(
            page_id=page.id,
            version=version.version,
            document=version.document,
            visitor_id=page.visitor_id,
        )

    @transaction.atomic
    def create(self, *, visitor_id, conversation_id, document) -> PageSnapshot:
        page = Page.objects.create(visitor_id=visitor_id, conversation_id=conversation_id)
        version = PageVersion.objects.create(
            page=page, version=1, document=document, author="agent"
        )
        return self._snapshot(page, version)

    def get(self, page_id: UUID) -> PageSnapshot:
        page = Page.objects.get(id=page_id)
        return self._snapshot(page, page.versions.get(version=page.current_version))

    def get_version(self, page_id: UUID, version: int) -> PageSnapshot:
        page = Page.objects.get(id=page_id)
        return self._snapshot(page, page.versions.get(version=version))

    @transaction.atomic
    def save_version(self, page_id, *, document, base_version, author) -> PageSnapshot:
        page = Page.objects.select_for_update().get(id=page_id)
        if page.current_version != base_version:
            raise VersionConflict(f"versión actual {page.current_version}, recibida {base_version}")
        page.current_version += 1
        page.save(update_fields=["current_version", "updated_at"])
        version = PageVersion.objects.create(
            page=page, version=page.current_version, document=document, author=author
        )
        return self._snapshot(page, version)


@cache
def _load_schema_file(name: str) -> dict:
    return json.loads((SCHEMA_DIR / name).read_text())


class FileSchemaProvider:
    """Lee los esquemas generados por `pnpm --filter @opzy/sections build:catalog`."""

    def page_schema(self) -> dict:
        return _load_schema_file("page-document.schema.json")

    def catalog(self) -> dict:
        return _load_schema_file("catalog.json")

    def library_version(self) -> str:
        return self.catalog()["library"]


class TrackingEventRecorder:
    def record(self, name: str, *, visitor_id, **refs) -> None:
        tracking.record(name, visitor_id=visitor_id, **refs)


def page_use_cases():
    from apps.pages.application.use_cases import PageUseCases

    return PageUseCases(DjangoPageRepository(), FileSchemaProvider(), TrackingEventRecorder())
