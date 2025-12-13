from django.contrib import admin
from property.models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    # Уберите 'owner' из search_fields
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']

    # Уберите метод get_owners пока
    # def get_owners(self, obj):
    #     ...


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
        try:
            return obj.flats.count()
        except:
            return 0

    get_flats_count.short_description = 'Кол-во квартир'