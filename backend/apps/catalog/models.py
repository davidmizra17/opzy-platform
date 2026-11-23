from django.db import models

from apps.common.models import BaseModel


class Package(BaseModel):
    """Paquete de Nivel 1 que el cliente puede comprar."""

    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price_cents = models.PositiveIntegerField()
    currency = models.CharField(max_length=3, default="USD")
    deposit_percent = models.PositiveSmallIntegerField(default=50)
    included_sections = models.JSONField(default=list, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
