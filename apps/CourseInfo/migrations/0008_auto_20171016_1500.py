# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 07:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CourseInfo', '0007_auto_20171016_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='课程类型')),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CourseInfo.Course_category', verbose_name='课程分类'),
        ),
        migrations.AlterField(
            model_name='course',
            name='click_num',
            field=models.IntegerField(default=0, verbose_name='点击数'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CourseInfo.Course_tag', verbose_name='课程方向'),
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('1', '初级'), ('2', '中级'), ('3', '高级')], default='1', max_length=10, verbose_name='课程难度'),
        ),
        migrations.AlterField(
            model_name='course',
            name='desc',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='课程简介'),
        ),
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=models.TextField(blank=True, null=True, verbose_name='课程详情'),
        ),
        migrations.AlterField(
            model_name='course',
            name='fav_num',
            field=models.IntegerField(default=0, verbose_name='收藏人数'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='course_image/%Y/%m', verbose_name='课程封面图'),
        ),
        migrations.AlterField(
            model_name='course',
            name='learn_num',
            field=models.IntegerField(default=0, verbose_name='学习人数'),
        ),
        migrations.AlterField(
            model_name='course',
            name='learn_time',
            field=models.IntegerField(default=0, verbose_name='学习时长'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=20, verbose_name='课程名称'),
        ),
        migrations.AlterField(
            model_name='course',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OrganizationInfo.Organization', verbose_name='所属机构'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OrganizationInfo.Teacher', verbose_name='所属讲师'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher_tell_you',
            field=models.TextField(blank=True, null=True, verbose_name='讲师通知'),
        ),
        migrations.AlterField(
            model_name='course',
            name='you_need_know',
            field=models.TextField(blank=True, null=True, verbose_name='课程须知'),
        ),
        migrations.AlterField(
            model_name='course_category',
            name='name',
            field=models.CharField(max_length=20, verbose_name='课程分类'),
        ),
        migrations.AlterField(
            model_name='course_tag',
            name='name',
            field=models.CharField(max_length=20, verbose_name='课程方向'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_style',
            field=models.ManyToManyField(blank=True, null=True, to='CourseInfo.Course_style', verbose_name='课程类型'),
        ),
    ]
