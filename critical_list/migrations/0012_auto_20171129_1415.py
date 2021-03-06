# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('critical_list', '0011_auto_20171126_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='pmc',
            field=models.CharField(
                choices=[('Arulselvan', 'HDT ENGINE'), ('Balaji', 'TRANSMISSION'), ('Joshna', 'AXLE'),
                         ('Giftson', 'MDT ENGINE'), ('Premkumar', 'CASTING AND FORGING')], help_text='Choose PMC',
                max_length=20),
        ),
        migrations.AlterField(
            model_name='part',
            name='shop',
            field=models.CharField(help_text='Enter Shop', max_length=30),
        ),
    ]
