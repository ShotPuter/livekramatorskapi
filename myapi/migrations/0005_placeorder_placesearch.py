# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-15 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_placeentertaiment_top'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_score', models.IntegerField(db_index=True, default=0)),
                ('num_vote_up', models.PositiveIntegerField(db_index=True, default=0)),
                ('num_vote_down', models.PositiveIntegerField(db_index=True, default=0)),
                ('name_place', models.CharField(max_length=500, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('tel', models.CharField(blank=True, max_length=100, verbose_name='Телефон')),
                ('adress', models.CharField(blank=True, max_length=200, verbose_name='Адрес')),
                ('working_time', models.CharField(blank=True, max_length=100, verbose_name='Время работы')),
                ('small_img', django_resized.forms.ResizedImageField(blank=True, upload_to='photos', verbose_name='Миниатюра')),
                ('high_img', django_resized.forms.ResizedImageField(blank=True, upload_to='photos', verbose_name='Полное фото')),
                ('link', models.CharField(blank=True, max_length=500, verbose_name='Ссылка')),
                ('category', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='myapi.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'Заказать',
                'verbose_name': 'Заказать',
            },
        ),
        migrations.CreateModel(
            name='PlaceSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_place', models.CharField(max_length=500, verbose_name='Название')),
                ('adress', models.CharField(blank=True, max_length=200, verbose_name='Адрес')),
                ('working_time', models.CharField(blank=True, max_length=100, verbose_name='Время работы')),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('category', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='myapi.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'Найти',
                'verbose_name': 'Найти',
            },
        ),
    ]