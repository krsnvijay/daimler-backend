# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 03:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('sos', '0002_auto_20171110_1703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sos',
            options={'ordering': ['-id'], 'permissions': (('can_change_status', 'Can Change Status'),)},
        ),
    ]
