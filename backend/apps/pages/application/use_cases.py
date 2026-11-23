"""Casos de uso de páginas. Vistas, agente y admin llaman a estas funciones."""

from uuid import UUID

from apps.pages.domain import document as doc
from apps.pages.domain.errors import UnsupportedClaims
from apps.pages.domain.facts import find_unsupported_claims

from .ports import EventRecorder, PageRepository, PageSnapshot, SchemaProvider


class PageUseCases:
    def __init__(self, repo: PageRepository, schemas: SchemaProvider, events: EventRecorder):
        self.repo = repo
        self.schemas = schemas
        self.events = events

    def create_page(
        self, *, visitor_id: UUID, conversation_id: UUID | None, locale: str = "es"
    ) -> PageSnapshot:
        document = doc.empty_document(
            library_version=self.schemas.library_version(), locale=locale
        )
        snapshot = self.repo.create(
            visitor_id=visitor_id, conversation_id=conversation_id, document=document
        )
        self.events.record("page_created", visitor_id=visitor_id, page_id=snapshot.page_id)
        return snapshot

    def update_page(
        self,
        page_id: UUID,
        *,
        operations: list[dict],
        base_version: int,
        client_facts: list[str],
        author: str = "agent",
    ) -> PageSnapshot:
        """Aplica cambios, valida esquema y regla de hechos, y guarda una versión nueva.

        Los errores vuelven al agente para que corrija su llamada antes de que
        el cliente vea nada.
        """
        current = self.repo.get(page_id)
        updated = doc.apply_patch(current.document, operations)
        doc.validate(updated, self.schemas.page_schema())
        claims = find_unsupported_claims(updated, client_facts)
        if claims:
            raise UnsupportedClaims(claims)
        snapshot = self.repo.save_version(
            page_id, document=updated, base_version=base_version, author=author
        )
        self.events.record(
            "page_updated",
            visitor_id=current.visitor_id,
            page_id=page_id,
            props={"version": snapshot.version, "ops": len(operations)},
        )
        return snapshot

    def revert_page(self, page_id: UUID, *, to_version: int, base_version: int) -> PageSnapshot:
        target = self.repo.get_version(page_id, to_version)
        snapshot = self.repo.save_version(
            page_id, document=target.document, base_version=base_version, author="client"
        )
        self.events.record(
            "page_reverted",
            visitor_id=target.visitor_id,
            page_id=page_id,
            props={"to_version": to_version},
        )
        return snapshot
