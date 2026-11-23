from django.contrib import admin

from .models import Page, PageVersion


class PageVersionInline(admin.TabularInline):
    model = PageVersion
    extra = 0
    can_delete = False
    readonly_fields = ("version", "author", "created_at", "document")


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Solo lectura del estado. Cambios de estado: acciones que llaman a los casos de uso."""

    list_display = ("id", "status", "current_version", "published_version", "subdomain")
    list_filter = ("status",)
    readonly_fields = ("status", "current_version", "published_version")
    inlines = [PageVersionInline]
