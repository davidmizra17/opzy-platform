# Django busca los modelos aquí; viven en infrastructure.
from apps.pages.infrastructure.models import Page, PageVersion

__all__ = ["Page", "PageVersion"]
