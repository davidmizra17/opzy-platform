from django.contrib import admin

from .models import Package


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("name", "price_cents", "currency", "is_active")
    prepopulated_fields = {"slug": ("name",)}
