# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 07:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserInfo', '0011_banner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '轮播图', 'verbose_name_plural': '轮播图'},
        ),
        migrations.AddField(
            model_name='banner',
            name='add_time',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='banner',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='banner/%Y/%m', verbose_name='轮播图'),
        ),
        migrations.AddField(
            model_name='banner',
            name='index',
            field=models.IntegerField(default=100, verbose_name='顺序'),
        ),
        migrations.AddField(
            model_name='banner',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='标题'),
        ),
        migrations.AddField(
            model_name='banner',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='访问地址'),
        ),
    ]
