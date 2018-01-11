# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-11 13:03
from __future__ import unicode_literals

import django.db.models.deletion
import jsonfield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0003_auto_20171129_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('subscription_id', jsonfield.fields.JSONField(default=dict)),
                ('user_id',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
