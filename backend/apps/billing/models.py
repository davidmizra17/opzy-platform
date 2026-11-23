from django.db import models

from apps.common.models import BaseModel


class Payment(BaseModel):
    """Pago a través del proveedor (checkout alojado). Se confirma solo por webhook."""

    class Status(models.TextChoices):
        PENDING = "pending"
        SUCCEEDED = "succeeded"
        FAILED = "failed"
        REFUNDED = "refunded"

    visitor_id = models.UUIDField(db_index=True)
    contact_id = models.UUIDField(null=True, blank=True)
    package_id = models.UUIDField()
    page_id = models.UUIDField(null=True, blank=True)
    amount_cents = models.PositiveIntegerField()
    currency = models.CharField(max_length=3, default="USD")
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.PENDING)
    provider = models.CharField(max_length=32)
    provider_reference = models.CharField(max_length=128, unique=True)
    idempotency_key = models.CharField(max_length=64, unique=True)
