import uuid

from django.db import models


class BaseModel(models.Model):
    """Base de todos los modelos: UUID como clave y marcas de tiempo."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
