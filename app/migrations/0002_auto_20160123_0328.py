# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 03:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Breed'),
        ),
    ]
