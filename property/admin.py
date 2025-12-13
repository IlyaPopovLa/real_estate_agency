from django.contrib import admin
from property.models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']
    extra = 0


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town', 'owner']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']
    inlines = [OwnerInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']
    list_display = ['user', 'flat', 'text']
    search_fields = ['user__username', 'flat__address', 'text']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    list_display = ['full_name', 'phonenumber', 'pure_phone', 'get_flats_count']
    search_fields = ['full_name', 'phonenumber', 'pure_phone']

    def get_flats_count(self, obj):
        return obj.flats.count()

    get_flats_count.short_description = 'Кол-во квартир'