from django.contrib import admin

from .models import Flat, Complaint


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    new_building = ['new_building']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town', 'owner_pure_phone']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony', 'owner_pure_phone']
    raw_id_fields = ['liked_by']


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']
    list_display = ['user', 'flat', 'text']
    search_fields = ['user__username', 'flat__address', 'text']