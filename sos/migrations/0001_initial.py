# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 10:50
from __future__ import unicode_literals

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now, help_text='Enter Level')),
                ('content', models.CharField(help_text='Enter Content', max_length=100)),
                ('media', models.FileField(blank=True, help_text='Media', upload_to='comment/%Y/%m/%d/')),
            ],
            options={
                'ordering': ['-uid'],
            },
        ),
        migrations.CreateModel(
            name='Sos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=50)),
                ('content', models.CharField(help_text='Enter Content', max_length=100)),
                ('media', models.FileField(blank=True, help_text='Media', upload_to='content/%Y/%m/%d/')),
                ('date', models.DateTimeField(default=datetime.datetime.now, help_text='Date', max_length=30)),
                ('level', models.IntegerField(help_text='Enter Level')),
                ('status', models.BooleanField(default=True, help_text='Open Or Closed')),
                ('posted_by',
                 models.ForeignKey(help_text='Uid', max_length=30, on_delete=django.db.models.deletion.CASCADE,
                                   related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(help_text='Employee Involved', related_name='employee_involved',
                                                 to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='sosid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sos.Sos'),
        ),
        migrations.AddField(
            model_name='comment',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
