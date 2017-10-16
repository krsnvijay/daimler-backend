from django.db import models

# Create your models here.
from django.urls import reverse
from import_export import resources, fields


class Part(models.Model):
    class Meta:
        ordering = ["-part_number"]

    part_number = models.CharField(max_length=30, primary_key=True, help_text='Enter Part Number')
    description = models.CharField(max_length=100, help_text='Enter Part\'s Description')
    supplier_name = models.CharField(max_length=50, help_text='Enter Supplier\'s Name')
    eta_dicv = models.CharField(max_length=30, help_text='Enter ETA')
    truck_details = models.CharField(max_length=30, help_text='Enter Truck Details')
    shortage_reason = models.CharField(max_length=100, help_text='Enter Reason For Shortage')
    delayed = models.BooleanField(help_text='Check if the part is delayed', default=False)

    def __str__(self):
        return self.part_number

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('model-detail-view', args=[str(self.part_number)])


class PartResource(resources.ModelResource):
    part_number = fields.Field(attribute="part_number", column_name='part number')
    description = fields.Field(attribute="description", column_name='description')
    supplier_name = fields.Field(attribute="supplier_name", column_name='Supplier Name')
    eta_dicv = fields.Field(attribute="eta_dicv", column_name='ETA DICV')
    truck_details = fields.Field(attribute="truck_details", column_name='Truck Details')
    shortage_reason = fields.Field(attribute="shortage_reason", column_name='Reason for shortage')

    class Meta:
        model = Part
        import_id_fields = ('part_number',)
        fields = ('part_number', 'description', 'supplier_name', 'eta_dicv', 'truck_details', 'shortage_reason')
        export_order = ('part_number', 'description', 'supplier_name', 'eta_dicv', 'truck_details', 'shortage_reason')
