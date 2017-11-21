# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('critical_list', '0009_auto_20171121_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='count',
            field=models.IntegerField(help_text='Enter count'),
        ),
        migrations.AlterField(
            model_name='part',
            name='planned_vehicle_qty',
            field=models.IntegerField(help_text='Enter planned vehicle quantity'),
        ),
        migrations.AlterField(
            model_name='part',
            name='quantity',
            field=models.IntegerField(help_text='Enter Quantity Avl DICV'),
        ),
        migrations.AlterField(
            model_name='part',
            name='quantity_expected',
            field=models.IntegerField(help_text='Enter quantity expected'),
        ),
        migrations.AlterField(
            model_name='part',
            name='status',
            field=models.IntegerField(choices=[(1, 'Normal'), (2, 'Warning'), (3, 'Critical')], default=1,
                                      help_text='Select the part Status'),
        ),
    ]
