# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseInfo', '0012_lesson_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]