# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-11 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0011_auto_20171111_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeentertaiment',
            name='city',
            field=models.CharField(max_length=1000, verbose_name='Координаты'),
        ),
        migrations.AlterField(
            model_name='placeentertaiment',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='48.737512197810915,397.5847434997558', max_length=63),
        ),
        migrations.AlterField(
            model_name='placesearch',
            name='city',
            field=models.CharField(max_length=1000, verbose_name='Координаты'),
        ),
        migrations.AlterField(
            model_name='placesearch',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='48.737512197810915,397.5847434997558', max_length=63),
        ),
    ]
