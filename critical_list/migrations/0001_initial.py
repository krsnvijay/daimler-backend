# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 10:50
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('part_number', models.CharField(help_text='Enter Part Number', max_length=30, primary_key=True, serialize=False)),
                ('description', models.CharField(help_text="Enter Part's Description", max_length=100)),
                ('supplier_name', models.CharField(help_text="Enter Supplier's Name", max_length=50)),
                ('variants', models.CharField(help_text='Enter Variants', max_length=30)),
                ('count', models.IntegerField(help_text='Enter count')),
                (
                'reported_on', models.DateField(default=datetime.datetime.now, help_text='Reported on', max_length=30)),
                ('short_on', models.DateField(default=datetime.datetime.now, help_text='Short on', max_length=30)),
                ('shop', models.CharField(choices=[('MDT ENGINE', 'MDT ENGINE'), ('HDT ENGINE', 'HDT ENGINE'),
                                                   ('TRANSMISSION', 'TRANSMISSION'),
                                                   ('CASTING AND FORGING', 'CASTING AND FORGING'), ('AXLE', 'AXLE')],
                                          help_text='Enter Text', max_length=30)),
                ('pmc', models.CharField(help_text='Enter PMC', max_length=20)),
                ('team', models.CharField(help_text='Enter Team', max_length=20)),
                ('backlog', models.CharField(help_text='Enter Backlog', max_length=10)),
                ('region', models.CharField(help_text='Enter Region', max_length=10)),
                ('unloading_point', models.CharField(help_text='Enter Unloading Point', max_length=5)),
                ('p_q', models.CharField(help_text='Enter P Q', max_length=1)),
                ('quantity', models.IntegerField(help_text='Enter Quantity Avl DICV')),
                ('quantity_expected', models.IntegerField(help_text='Enter quantity expected')),
                ('planned_vehicle_qty', models.IntegerField(help_text='Enter planned vehicle quantity')),
                ('eta_dicv', models.CharField(help_text='Enter ETA', max_length=30)),
                ('truck_details', models.CharField(help_text='Enter Truck Details', max_length=30)),
                ('shortage_reason', models.CharField(help_text='Enter Reason For Shortage', max_length=100)),
                ('status', models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Warning', 'Warning'),
                                                                 ('Critical', 'Critical')],
                                            help_text='Select the part Status', max_length=10)),
            ],
            options={
                'ordering': ['-part_number'],
            },
        ),
    ]
