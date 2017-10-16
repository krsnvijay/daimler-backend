from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from app.models import PartResource, Part

@admin.register(Part)
class PartAdmin(ImportExportModelAdmin):
    resource_class = PartResource
    search_fields = ['part_number', 'supplier_name','truck_details']
    list_filter = ('supplier_name', 'truck_details')
    list_display = ('part_number', 'description', 'supplier_name', 'eta_dicv','truck_details','shortage_reason')