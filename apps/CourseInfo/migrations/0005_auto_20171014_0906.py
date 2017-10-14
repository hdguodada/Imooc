# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 01:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
        ('CourseInfo', '0004_course_click_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operation.Course_category'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operation.Course_tag'),
        ),
        migrations.AddField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('1', 'level 1'), ('2', 'level 2'), ('3', 'level 3')], default='1', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='desc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_tell_you',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='you_need_know',
            field=models.TextField(blank=True, null=True),
        ),
    ]
