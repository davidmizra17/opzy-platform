"""API interna de tracking: cualquier módulo registra eventos con `record`."""

import uuid
from datetime import datetime
from uuid import UUID

from django.utils import timezone

from .catalog import EVENT_NAMES
from .models import Event


class UnknownEvent(ValueError):
    pass


def record(
    name: str,
    *,
    visitor_id: UUID,
    source: str = "backend",
    occurred_at: datetime | None = None,
    event_id: UUID | None = None,
    **refs,
) -> Event:
    if name not in EVENT_NAMES:
        raise UnknownEvent(name)
    props = refs.pop("props", {})
    event, _ = Event.objects.get_or_create(
        event_id=event_id or uuid.uuid4(),
        defaults={
            "name": name,
            "source": source,
            "occurred_at": occurred_at or timezone.now(),
            "visitor_id": visitor_id,
            "props": props,
            **refs,
        },
    )
    return event
