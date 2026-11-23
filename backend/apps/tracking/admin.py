from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "source", "visitor_id", "occurred_at")
    list_filter = ("name", "source")
    search_fields = ("visitor_id", "conversation_id")
