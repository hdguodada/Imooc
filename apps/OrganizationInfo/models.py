from django.db import models
from datetime import datetime

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=(('pxjg', 'pxjg'), ('gr', 'gr'), ('gx', 'gx')), default='pxjg')
    tag = models.CharField(default='good', max_length=50)
    click_nums = models.IntegerField(default=0)
    fav_nums = models.IntegerField(default=0)
    image = models.ImageField(upload_to='organization/%Y/%m', default='')
    address = models.CharField(max_length=100, null=True, blank=True)
    students = models.IntegerField(default=0)
    add_time = models.DateTimeField(default=datetime.now)
    city = models.ForeignKey(CityDict, null=True, blank=True)

    def get_course_num(self):
        return self.course_set.all().count()

    def get_teacher_num(self):
        return self.teacher_set.all().count()

    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name="teacher's name")
    organization = models.ForeignKey(Organization, null=True, blank=True)
    work_years = models.IntegerField(default=0)
    work_company = models.CharField(max_length=100)
    work_position = models.CharField(max_length=100)
    poits = models.CharField(max_length=50, verbose_name='hao teach')
    click_nums = models.IntegerField(default=0)
    fav_nums = models.IntegerField(default=0)
    age = models.IntegerField(default=30)
    image = models.ImageField(upload_to='teacher/%Y/%m', null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now)

    def get_course_nums(self):
        return self.course_set.all().count()

    def __str__(self):
        return self.name
