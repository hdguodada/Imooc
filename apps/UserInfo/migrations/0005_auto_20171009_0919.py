# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserInfo', '0004_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailverifyrecord',
            options={'verbose_name_plural': 'emailcode'},
        ),
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name_plural': 'usermessage'},
        ),
        migrations.AddField(
            model_name='emailverifyrecord',
            name='has_user',
            field=models.BooleanField(default=False),
        ),
    ]