from django.db import models
from OrganizationInfo.models import Organization, Teacher
from datetime import datetime

# Create your models here.

# 课程方向
class Course_tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='课程方向')
    course = models.ManyToManyField('Course', related_name='course_tags')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程方向'
        verbose_name_plural = verbose_name


# 课程分类
class Course_category(models.Model):
    name = models.CharField(max_length=20, verbose_name='课程分类')
    course = models.ManyToManyField('Course', related_name='course_categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程分类'
        verbose_name_plural = verbose_name


# 课程类型
class Course_style(models.Model):
    name = models.CharField(max_length=20, verbose_name='课程类型')
    course = models.ManyToManyField('Course', related_name='course_styles')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程类型'
        verbose_name_plural = verbose_name



# 课程
class Course(models.Model):
    name = models.CharField(max_length=20, verbose_name='课程名称')
    learn_time = models.IntegerField(default=0, verbose_name='学习时长')
    image = models.ImageField(null=True, blank=True, upload_to='course_image/%Y/%m', verbose_name='课程封面图')
    learn_num = models.IntegerField(default=0, verbose_name='学习人数')
    fav_num = models.IntegerField(default=0, verbose_name='收藏人数')
    organization = models.ForeignKey(Organization, null=True, blank=True, verbose_name='所属机构')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    desc = models.CharField(max_length=200, null=True, blank=True, verbose_name='课程简介')
    detail = models.TextField(null=True, blank=True, verbose_name='课程详情')
    you_need_know = models.TextField(null=True, blank=True, verbose_name='课程须知')
    teacher_tell_you = models.TextField(null=True, blank=True, verbose_name='讲师通知')
    degree= models.CharField(choices=(('1', '初级'), ('2', '中级'), ('3', '高级')), max_length=10, default='1', verbose_name='课程难度')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    teacher = models.ForeignKey(Teacher, blank=True, null=True, verbose_name='所属讲师')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name



