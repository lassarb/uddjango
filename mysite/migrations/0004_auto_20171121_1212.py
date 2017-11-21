# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20171120_1514'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizza',
            options={'ordering': ['name'], 'verbose_name': 'Пицца', 'verbose_name_plural': 'Пиццы'},
        ),
        migrations.AddField(
            model_name='pizza',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='mysite/photos', verbose_name='Фото'),
        ),
    ]