# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseInfo', '0014_auto_20171023_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name': 'banner_course',
                'proxy': True,
                'indexes': [],
            },
            bases=('CourseInfo.course',),
        ),
        migrations.AddField(
            model_name='course',
            name='is_banner',
            field=models.BooleanField(default=False),
        ),
    ]