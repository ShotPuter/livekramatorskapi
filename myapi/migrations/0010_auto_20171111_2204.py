# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-11 20:04
from __future__ import unicode_literals

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0009_auto_20171111_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeentertaiment',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63),
        ),
    ]
