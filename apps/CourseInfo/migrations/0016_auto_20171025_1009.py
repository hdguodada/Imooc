# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 02:09
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CourseInfo', '0015_auto_20171024_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='课程详情'),
        ),
    ]