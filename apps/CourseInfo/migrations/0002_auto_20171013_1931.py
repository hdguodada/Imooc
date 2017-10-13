# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseInfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='course_image/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='course',
            name='learn_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='learn_time',
            field=models.IntegerField(default=0),
        ),
    ]
