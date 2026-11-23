from django.db import models

from apps.common.models import BaseModel


class Organization(BaseModel):
    """El negocio del cliente."""

    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=2, blank=True)

    def __str__(self) -> str:
        return self.name


class Contact(BaseModel):
    """Una persona real, creada cuando deja su contacto o paga."""

    organization = models.ForeignKey(
        Organization, null=True, blank=True, on_delete=models.SET_NULL, related_name="contacts"
    )
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True, db_index=True)
    whatsapp = models.CharField(max_length=32, blank=True, db_index=True)
    consent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name or self.email or self.whatsapp or str(self.id)


class Visitor(BaseModel):
    """Visitante anónimo. Se une a un Contact al identificarse."""

    contact = models.ForeignKey(
        Contact, null=True, blank=True, on_delete=models.SET_NULL, related_name="visitors"
    )
    language = models.CharField(max_length=8, default="es")
    first_seen_at = models.DateTimeField(auto_now_add=True)


class Session(BaseModel):
    """Una visita, con su origen (UTM)."""

    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, related_name="sessions")
    token = models.CharField(max_length=64, unique=True)
    utm = models.JSONField(default=dict, blank=True)
    user_agent = models.TextField(blank=True)
    expires_at = models.DateTimeField()
