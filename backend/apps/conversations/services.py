"""API interna de conversations."""

from datetime import timedelta
from uuid import UUID

from django.conf import settings
from django.db import transaction
from django.db.models import F
from django.utils import timezone

from apps.tracking import services as tracking

from .models import Conversation, Message


class LimitReached(Exception):
    """Se alcanzó un límite de uso. El widget ofrece seguir con una persona."""


def start_conversation(*, visitor_id: UUID, language: str = "es") -> Conversation:
    since = timezone.now() - timedelta(days=1)
    today = Conversation.objects.filter(visitor_id=visitor_id, created_at__gte=since).count()
    if today >= settings.MAX_CONVERSATIONS_PER_VISITOR_PER_DAY:
        raise LimitReached("conversations_per_day")
    conversation = Conversation.objects.create(visitor_id=visitor_id, language=language)
    tracking.record("widget_opened", visitor_id=visitor_id, conversation_id=conversation.id)
    return conversation


@transaction.atomic
def add_client_message(conversation: Conversation, text: str) -> Message:
    message = Message.objects.create(
        conversation=conversation, role=Message.Role.CLIENT, text=text
    )
    tracking.record(
        "message_sent", visitor_id=conversation.visitor_id, conversation_id=conversation.id
    )
    return message


@transaction.atomic
def add_agent_message(conversation: Conversation, text: str) -> Message:
    if conversation.agent_turns >= settings.MAX_AGENT_TURNS_PER_CONVERSATION:
        raise LimitReached("agent_turns")
    Conversation.objects.filter(id=conversation.id).update(agent_turns=F("agent_turns") + 1)
    return Message.objects.create(conversation=conversation, role=Message.Role.AGENT, text=text)


def history(conversation_id: UUID) -> list[dict]:
    return list(
        Message.objects.filter(conversation_id=conversation_id).values("role", "text", "created_at")
    )
