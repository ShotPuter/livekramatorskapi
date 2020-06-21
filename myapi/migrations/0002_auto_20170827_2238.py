# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-27 19:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceEntertaiment',
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
                ('special_offers', models.IntegerField(default=1, verbose_name='Количество предложений')),
                ('link', models.CharField(blank=True, max_length=500, verbose_name='Ссылка')),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
        migrations.RemoveField(
            model_name='place',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=1, upload_to='category_image', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='place_loc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapi.PlaceEntertaiment', verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='poster',
            name='place_loc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapi.PlaceEntertaiment', verbose_name='Место'),
        ),
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.AddField(
            model_name='placeentertaiment',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='myapi.Category', verbose_name='Категория'),
        ),
    ]