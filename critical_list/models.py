# Create your models here.
from datetime import datetime

from django.db import models
# Create your models here.
from django.urls import reverse
from import_export import resources


class Part(models.Model):
    values = (('MDT ENGINE', 'MDT ENGINE'), ('HDT ENGINE', 'HDT ENGINE'), ('TRANSMISSION', 'TRANSMISSION'), (
        'CASTING AND FORGING', 'CASTING AND FORGING'), ('AXLE', 'AXLE'))
    CRITICAL = 3
    WARNING = 2
    NORMAL = 1
    statusvalues = (
        (NORMAL, 'Normal'),
        (WARNING, 'Warning'),
        (CRITICAL, 'Critical'),
    )

    class Meta:
        ordering = ["-part_number"]
        permissions = (
            ("can_change_status", "Can Change Status"),
        )

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
    status = models.IntegerField(choices=statusvalues, help_text='Select the part Status', default=NORMAL)

    def __str__(self):
        return self.part_number

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('part-detail', args=[str(self.part_number)])


class PartResource(resources.ModelResource):
    class Meta:
        import_id_fields = ('part_number',)
        model = Part
