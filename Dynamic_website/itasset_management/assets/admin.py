from django.contrib import admin
from .models import Asset, AssetAssignment
# Register your models here.
@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):

    list_display = (
        'asset_id',
        'asset_type',
        'manufacturer',
        'model',
        'serial_number',
        'status',
        'location',
    )

    search_fields = (
        'asset_id',
        'serial_number',
        'manufacturer',
        'model',
    )

    list_filter = (
        'asset_type',
        'status',
    )


@admin.register(AssetAssignment)
class AssetAssignmentAdmin(admin.ModelAdmin):

    list_display = (
        'asset',
        'employee',
        'assigned_date',
        'returned_date',
        'status',
    )

    list_filter = (
        'status',
    )