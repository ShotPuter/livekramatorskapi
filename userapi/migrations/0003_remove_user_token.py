# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-17 19:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0002_auto_20170915_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='token',
        ),
    ]