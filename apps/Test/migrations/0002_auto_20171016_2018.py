# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='authors', to='Test.Author'),
        ),
    ]
