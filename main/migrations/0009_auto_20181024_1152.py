# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-24 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_store_reset_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='reset_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]