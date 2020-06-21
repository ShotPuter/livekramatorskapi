# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-31 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('category_choice', models.CharField(choices=[('Search', 'Найти'), ('Order', 'Заказать'), ('Entertaiment', 'Развлечения')], default='Search', max_length=100, verbose_name='Раздел')),
            ],
            options={
                'verbose_name_plural': 'Категории',
                'verbose_name': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
                ('date', models.DateField(verbose_name='Дата сортировки')),
                ('link', models.CharField(max_length=1000, verbose_name='Источник')),
                ('card', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Миниатюра')),
                ('photo', django_resized.forms.ResizedImageField(upload_to='photos', verbose_name='Полное фото')),
            ],
            options={
                'verbose_name_plural': 'Мероприятия',
                'verbose_name': 'Мероприятие',
            },
        ),
        migrations.CreateModel(
            name='Koordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
                ('news_choice', models.CharField(choices=[('Police', 'Полиция'), ('Sport', 'Спорт'), ('Live', 'Общественная жизнь'), ('GorAdmin', 'Городская администрация'), ('City', 'Благоустройство города'), ('Study', 'Образование'), ('Important', 'Важное')], default='Live', max_length=100)),
                ('date', models.DateField(verbose_name='Дата')),
                ('link', models.CharField(max_length=1000, verbose_name='Источник')),
                ('card', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Миниатюра')),
                ('photo', django_resized.forms.ResizedImageField(upload_to='photos', verbose_name='Полное фото')),
            ],
            options={
                'verbose_name_plural': 'Новости',
                'verbose_name': 'Новость',
            },
        ),
        migrations.CreateModel(
            name='Place',
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
                ('special_offers', models.IntegerField(default=1, verbose_name='Количество предложений(не может пустовать)')),
                ('link', models.CharField(blank=True, max_length=500, verbose_name='Ссылка')),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('category', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='myapi.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'Места',
                'verbose_name': 'Место',
            },
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Название')),
                ('vid', models.CharField(choices=[('Kino', 'Кино'), ('Concert', 'Концерт'), ('Teatr', 'Театр')], max_length=500, verbose_name='Вид постера')),
                ('description', models.TextField(verbose_name='Описание')),
                ('types', models.CharField(max_length=500, verbose_name='Жанры')),
                ('actors', models.TextField(verbose_name='Актеры')),
                ('seans', models.TextField(verbose_name='Сеансы')),
                ('language', models.CharField(max_length=500, verbose_name='Язык показа')),
                ('time', models.CharField(max_length=500, verbose_name='Время показа')),
                ('cost', models.CharField(max_length=100, verbose_name='Цена показа')),
                ('date', models.DateField(verbose_name='Дата')),
                ('link', models.CharField(max_length=1000, verbose_name='YouTube')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Постер фото')),
                ('full_photo', django_resized.forms.ResizedImageField(upload_to='photos', verbose_name='Полное фото')),
                ('place_loc', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapi.Place', verbose_name='Место')),
            ],
            options={
                'verbose_name_plural': 'Афиша',
                'verbose_name': 'Постер',
            },
        ),
        migrations.CreateModel(
            name='Way',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Название')),
                ('pk_way', models.CharField(max_length=30, verbose_name='Передаваемое имя')),
            ],
            options={
                'verbose_name_plural': 'Маршруты',
                'verbose_name': 'Маршрут',
            },
        ),
        migrations.AddField(
            model_name='koordinates',
            name='way',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.Way'),
        ),
        migrations.AddField(
            model_name='event',
            name='place_loc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapi.Place', verbose_name='Место'),
        ),
    ]
