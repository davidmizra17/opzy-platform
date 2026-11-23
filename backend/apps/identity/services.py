"""API interna de identity. Otros módulos usan estas funciones, no los modelos."""

import secrets
from datetime import timedelta
from uuid import UUID

from django.utils import timezone

from .models import Session, Visitor

SESSION_TTL = timedelta(days=30)


def start_session(*, visitor_id: UUID | None, utm: dict, user_agent: str) -> Session:
    visitor = Visitor.objects.filter(id=visitor_id).first() if visitor_id else None
    if visitor is None:
        visitor = Visitor.objects.create()
    return Session.objects.create(
        visitor=visitor,
        token=secrets.token_urlsafe(32),
        utm=utm,
        user_agent=user_agent[:500],
        expires_at=timezone.now() + SESSION_TTL,
    )


def resolve_session(token: str) -> Session | None:
    return (
        Session.objects.select_related("visitor")
        .filter(token=token, expires_at__gt=timezone.now())
        .first()
    )
