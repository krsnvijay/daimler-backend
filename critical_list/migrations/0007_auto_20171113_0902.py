# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 03:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('critical_list', '0006_auto_20171112_0911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='part',
            options={'ordering': ['-part_number'], 'permissions': (('can_change_status', 'Can Change Status'),)},
        ),
    ]
