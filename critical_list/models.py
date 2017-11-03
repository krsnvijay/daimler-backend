# Create your models here.
from datetime import datetime

from django.db import models
# Create your models here.
from django.urls import reverse
from import_export import resources, fields


class Part(models.Model):
    values = (('MDT ENGINE', 'MDT ENGINE'), ('HDT ENGINE', 'HDT ENGINE'), ('TRANSMISSION', 'TRANSMISSION'), (
        'CASTING AND FORGING', 'CASTING AND FORGING'), ('AXLE', 'AXLE'))
    CRITICAL = 'Critical'
    WARNING = 'Warning'
    statusvalues = (
        (CRITICAL, 'Critical'),
        (WARNING, 'Warning'))

    class Meta:
        ordering = ["-part_number"]

    part_number = models.CharField(max_length=30, primary_key=True, help_text='Enter Part Number')
    description = models.CharField(max_length=100, help_text='Enter Part\'s Description')
    supplier_name = models.CharField(max_length=50, help_text='Enter Supplier\'s Name')
    variants = models.CharField(max_length=30, help_text='Enter Variants')
    count = models.IntegerField(help_text='Enter count')
    reported_on = models.DateField(max_length=30, help_text='Reported on', default=datetime.now)
    short_on = models.DateField(max_length=30, help_text='Short on', default=datetime.now)
    shop = models.CharField(max_length=30, choices=values, help_text='Enter Text')
    pmc = models.CharField(max_length=20, help_text='Enter PMC')
    team = models.CharField(max_length=20, help_text='Enter Team')
    backlog = models.CharField(max_length=10, help_text='Enter Backlog')
    region = models.CharField(max_length=10, help_text='Enter Region')
    unloading_point = models.CharField(max_length=5, help_text='Enter Unloading Point')
    p_q = models.CharField(max_length=1, help_text='Enter P Q')
    quantity = models.IntegerField(help_text='Enter Quantity Avl DICV')
    quantity_expected = models.IntegerField(help_text='Enter quantity expected')
    planned_vehicle_qty = models.IntegerField(help_text='Enter planned vehicle quantity')
    eta_dicv = models.CharField(max_length=30, help_text='Enter ETA')
    truck_details = models.CharField(max_length=30, help_text='Enter Truck Details')
    shortage_reason = models.CharField(max_length=100, help_text='Enter Reason For Shortage')
    status = models.CharField(max_length=10, choices=statusvalues, help_text='Select the part Status', blank=True)
    starred = models.BooleanField(help_text='Check if the part is Starred', default=False)

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
