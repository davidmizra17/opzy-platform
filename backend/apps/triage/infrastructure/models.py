from django.db import models

from apps.common.models import BaseModel


class ProblemRecordModel(BaseModel):
    """Versión persistida del registro. Cada corrección del cliente crea una fila nueva."""

    conversation_id = models.UUIDField(db_index=True)
    version = models.PositiveIntegerField()
    data = models.JSONField()
    route = models.CharField(max_length=8, blank=True)
    needs_human = models.BooleanField(default=False)

    class Meta:
        app_label = "triage"
        constraints = [
            models.UniqueConstraint(
                fields=["conversation_id", "version"], name="unique_problem_record_version"
            )
        ]
