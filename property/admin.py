from django.contrib import admin

from .models import Complaint, Flat, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'owner', 'address']
    readonly_fields = ['created_at']
    list_display = (
        'address',
        'price',
        'owners_phonenumber',
        'owner_pure_phone',
        'new_building',
        'construction_year',
        'town'
    )
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['liked_by']
    inlines = [OwnerInline]
    exclude = ['flats']


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
