# Create your models here.
from datetime import datetime

from django.db import models
# Create your models here.
from django.urls import reverse
from import_export import resources, fields, widgets


class Part(models.Model):
    CRITICAL = 3
    WARNING = 2
    NORMAL = 1
    pmc_values = (
        ('Arulselvan', 'HDT ENGINE'),
        ('Balaji', 'TRANSMISSION'),
        ('Joshna', 'AXLE'),
        ('Giftson', 'MDT ENGINE'),
        ('Premkumar', 'CASTING AND FORGING'),
    )
    unloading_point_values = (
        ('LC', 'LC'),
        ('DOL', 'DOL'),
        ('FS', 'FS'),
        ('Chennai', 'Chennai')
    )
    team_values = (
        ('Import', 'Import'),
        ('PTI', 'PTI'),
        ('Bus', 'Bus'),
        ('Vehicle', 'Vehicle')
    )
    region_values = (
        ('Import', 'Import'),
        ('Chennai', 'Chennai'),
        ('North', 'North'),
        ('South', 'South'),
        ('West', 'West'),
        ('East', 'East')
    )
    status_values = (
        (NORMAL, 'Normal'),
        (WARNING, 'Warning'),
        (CRITICAL, 'Critical'),
    )
    p_q_values = (
        ('Y', 'Y'),
        ('N', 'N')
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
    shop = models.CharField(max_length=30, help_text='Enter Shop')
    pmc = models.CharField(max_length=20, choices=pmc_values, help_text='Choose PMC')
    team = models.CharField(max_length=10, choices=team_values, help_text='Enter Team')
    backlog = models.CharField(max_length=10, help_text='Enter Backlog')
    region = models.CharField(max_length=10, choices=region_values, help_text='Enter Region')
    unloading_point = models.CharField(max_length=10, choices=unloading_point_values, help_text='Enter Unloading Point')
    p_q = models.CharField(max_length=1, help_text='Enter P Q', choices=p_q_values, default='N')
    quantity = models.IntegerField(help_text='Enter Quantity Avl DICV')
    quantity_expected = models.IntegerField(help_text='Enter quantity expected')
    planned_vehicle_qty = models.IntegerField(help_text='Enter planned vehicle quantity')
    eta_dicv = models.CharField(max_length=50, help_text='Enter ETA')
    truck_details = models.CharField(max_length=30, help_text='Enter Truck Details', null=True, blank=True)
    shortage_reason = models.CharField(max_length=100, help_text='Enter Reason For Shortage', null=True, blank=True)
    status = models.IntegerField(choices=status_values, help_text='Select the part Status', default=NORMAL)

    def __str__(self):
        return self.part_number

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('part-detail', args=[str(self.part_number)])


class PartResource(resources.ModelResource):
    part_number = fields.Field(attribute="part_number", column_name='Part number')
    description = fields.Field(attribute="description", column_name='Description')
    supplier_name = fields.Field(attribute="supplier_name", column_name='Supplier')
    variants = fields.Field(attribute="variants", column_name='Variants')
    count = fields.Field(attribute="count", column_name='Count')
    reported_on = fields.Field(attribute="reported_on", column_name='Reported on ( dd/mm/yy )',
                               widget=widgets.DateWidget(format='%d-%b-%y'))
    short_on = fields.Field(attribute="short_on", column_name='Short on ( dd/mm/yy )',
                            widget=widgets.DateWidget(format='%d-%b-%y'))
    shop = fields.Field(attribute="shop", column_name='Shop')
    pmc = fields.Field(attribute="pmc", column_name='PMC')
    team = fields.Field(attribute="team", column_name='Team')
    backlog = fields.Field(attribute="backlog", column_name='Backlog')
    region = fields.Field(attribute="region", column_name='Region')
    unloading_point = fields.Field(attribute="unloading_point", column_name='Unloadingpoint')
    p_q = fields.Field(attribute="p_q", column_name='PQ indiator')
    quantity = fields.Field(attribute="quantity", column_name='Quantity Avl DICV (vehicle#scovered)')
    quantity_expected = fields.Field(attribute="quantity_expected", column_name='Outlook')
    planned_vehicle_qty = fields.Field(attribute="planned_vehicle_qty", column_name='Plan')
    eta_dicv = fields.Field(attribute="eta_dicv", column_name='ETA')
    truck_details = fields.Field(attribute="truck_details", column_name='Truck details')
    shortage_reason = fields.Field(attribute="shortage_reason", column_name='Reason for shortage')
    status = fields.Field(attribute="status", column_name='Status')
    class Meta:
        import_id_fields = ('part_number',)
        model = Part
        widgets = {
            'reported_on': {'format': '%d-%b-%y'},
            'short_on': {'format': '%d-%b-%y'},
        }
