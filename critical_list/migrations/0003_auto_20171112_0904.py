# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('critical_list', '0002_auto_20171112_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='shop',
            field=models.CharField(
                choices=[('MDT ENGINE', 'MDT ENGINE'), ('HDT ENGINE', 'HDT ENGINE'), ('TRANSMISSION', 'TRANSMISSION'),
                         ('CASTING AND FORGING', 'CASTING AND FORGING'), ('AXLE', 'AXLE')], help_text='Enter Text',
                max_length=30),
        ),
        migrations.AlterField(
            model_name='part',
            name='status',
            field=models.CharField(choices=[(1, 'Normal'), (2, 'Warning'), (3, 'Critical')], default=1,
                                   help_text='Select the part Status', max_length=10),
        ),
    ]
