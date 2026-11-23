from django.db import models

from apps.common.models import BaseModel


class Page(BaseModel):
    class Status(models.TextChoices):
        DRAFT = "draft"
        APPROVED = "approved"
        PUBLISHED = "published"

    visitor_id = models.UUIDField(db_index=True)
    conversation_id = models.UUIDField(null=True, blank=True)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.DRAFT)
    current_version = models.PositiveIntegerField(default=1)
    published_version = models.PositiveIntegerField(null=True, blank=True)
    subdomain = models.SlugField(max_length=63, unique=True, null=True, blank=True)

    class Meta:
        app_label = "pages"

    def __str__(self) -> str:
        return f"Página {self.id} ({self.status})"


class PageVersion(models.Model):
    """Versión inmutable del documento. Deshacer = volver a una versión anterior."""

    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="versions")
    version = models.PositiveIntegerField()
    document = models.JSONField()
    author = models.CharField(max_length=16)  # agent | client | staff
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "pages"
        constraints = [
            models.UniqueConstraint(fields=["page", "version"], name="unique_page_version")
        ]
        ordering = ["page", "-version"]

    def __str__(self) -> str:
        return f"{self.page_id} v{self.version}"
