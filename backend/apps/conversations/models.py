from django.db import models

from apps.common.models import BaseModel


class Conversation(BaseModel):
    """Una conversación de intake. El portal (Fase 2) reutiliza la misma conversación."""

    class Status(models.TextChoices):
        OPEN = "open"
        WITH_HUMAN = "with_human"
        CLOSED = "closed"

    visitor_id = models.UUIDField(db_index=True)
    contact_id = models.UUIDField(null=True, blank=True)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.OPEN)
    language = models.CharField(max_length=8, default="es")
    agent_turns = models.PositiveIntegerField(default=0)


class Message(BaseModel):
    class Role(models.TextChoices):
        CLIENT = "client"
        AGENT = "agent"
        HUMAN = "human"
        SYSTEM = "system"

    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name="messages"
    )
    role = models.CharField(max_length=8, choices=Role.choices)
    text = models.TextField(blank=True)
    attachments = models.JSONField(default=list, blank=True)

    class Meta:
        ordering = ["created_at"]
