from django.contrib import admin
from .models import Product, Alert, WaterLevel, IncidentReport


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "created_by", "created_at")
    search_fields = ("name", "description")


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "created_at")
    list_filter = ("type",)
    search_fields = ("title", "message")


@admin.register(WaterLevel)
class WaterLevelAdmin(admin.ModelAdmin):
    list_display = ("location_name", "current_level", "status", "trend", "last_updated")
    list_filter = ("status", "trend")
    search_fields = ("location_name",)


@admin.register(IncidentReport)
class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ("reporter_name", "incident_type", "location", "created_at")
    list_filter = ("incident_type",)
    search_fields = ("reporter_name", "location", "incident_type")
