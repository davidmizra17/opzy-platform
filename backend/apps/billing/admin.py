from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "amount_cents", "currency", "status", "provider", "created_at")
    list_filter = ("status", "provider")
