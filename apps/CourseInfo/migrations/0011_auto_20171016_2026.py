# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseInfo', '0010_auto_20171016_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_style',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_tag',
        ),
        migrations.AddField(
            model_name='course_category',
            name='course',
            field=models.ManyToManyField(related_name='course_categories', to='CourseInfo.Course'),
        ),
        migrations.AddField(
            model_name='course_style',
            name='course',
            field=models.ManyToManyField(related_name='course_styles', to='CourseInfo.Course'),
        ),
        migrations.AddField(
            model_name='course_tag',
            name='course',
            field=models.ManyToManyField(related_name='course_tags', to='CourseInfo.Course'),
        ),
    ]
