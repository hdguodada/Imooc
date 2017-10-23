# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 07:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CourseInfo', '0013_video_video_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('download', models.FileField(upload_to='course/resource/%Y/%m')),
                ('add_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50, verbose_name='课程名称'),
        ),
        migrations.AddField(
            model_name='courseresource',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CourseInfo.Course'),
        ),
    ]
