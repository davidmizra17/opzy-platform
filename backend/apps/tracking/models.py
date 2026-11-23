from django.db import models


class Event(models.Model):
    """Registro de solo inserción. Las correcciones son eventos nuevos, nunca ediciones.

    Particionar por mes cuando el volumen lo pida (ver docs/adr).
    """

    event_id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=64, db_index=True)
    source = models.CharField(max_length=16)  # landing | widget | backend | webhook
    occurred_at = models.DateTimeField()
    received_at = models.DateTimeField(auto_now_add=True, db_index=True)
    visitor_id = models.UUIDField(db_index=True)
    session_id = models.UUIDField(null=True, blank=True)
    contact_id = models.UUIDField(null=True, blank=True, db_index=True)
    conversation_id = models.UUIDField(null=True, blank=True, db_index=True)
    page_id = models.UUIDField(null=True, blank=True)
    path = models.CharField(max_length=500, blank=True)
    props = models.JSONField(default=dict, blank=True)
    schema_version = models.PositiveSmallIntegerField(default=1)

    class Meta:
        indexes = [models.Index(fields=["visitor_id", "occurred_at"])]

    def __str__(self) -> str:
        return f"{self.name} @ {self.occurred_at:%Y-%m-%d %H:%M}"
