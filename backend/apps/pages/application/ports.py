"""Puertos que la capa de aplicación necesita. Infrastructure los implementa."""

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID


@dataclass(frozen=True)
class PageSnapshot:
    page_id: UUID
    version: int
    document: dict
    visitor_id: UUID


class PageRepository(Protocol):
    def create(
        self, *, visitor_id: UUID, conversation_id: UUID | None, document: dict
    ) -> PageSnapshot: ...

    def get(self, page_id: UUID) -> PageSnapshot: ...

    def get_version(self, page_id: UUID, version: int) -> PageSnapshot: ...

    def save_version(
        self, page_id: UUID, *, document: dict, base_version: int, author: str
    ) -> PageSnapshot: ...


class SchemaProvider(Protocol):
    def page_schema(self) -> dict: ...

    def library_version(self) -> str: ...


class EventRecorder(Protocol):
    def record(self, name: str, *, visitor_id: UUID, **refs) -> None: ...
