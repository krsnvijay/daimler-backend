# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 10:22
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sos', '0006_auto_20171118_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='userid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]