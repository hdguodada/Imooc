from django.db import models
from OrganizationInfo.models import Organization
from operation.models import Course_tag, Course_category
from datetime import datetime

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=20)
    learn_time = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to='course_image/%Y/%m')
    learn_num = models.IntegerField(default=0)
    fav_num = models.IntegerField(default=0)
    organization = models.ForeignKey(Organization)
    click_num = models.IntegerField(default=0)
    desc = models.CharField(max_length=200, null=True, blank=True)
    course_tag = models.ForeignKey(Course_tag, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Course_category, null=True, blank=True)
    you_need_know = models.TextField(null=True, blank=True)
    teacher_tell_you = models.TextField(null=True, blank=True)
    degree= models.CharField(choices=(('1', 'level 1'), ('2', 'level 2'), ('3', 'level 3')), max_length=10, default='1')
    add_time = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name
