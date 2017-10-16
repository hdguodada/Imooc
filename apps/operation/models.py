from django.db import models

# Create your models here.
from datetime import datetime
from UserInfo.models import UserProfile
from CourseInfo.models import Course




class UserAsk(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=12)
    course_name = models.CharField(max_length=50)
    add_time = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile)
    course = models.ForeignKey(Course)
    comments = models.TextField()
    add_time = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.user.username



class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile)
    fav_id = models.IntegerField(default=0)
    fav_type = models.IntegerField(choices=(('1', 'course'), ('2', 'organization'), ('3', 'teacher')))
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile)
    course = models.ForeignKey(Course)
    add_time = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.user.username


class UserMessage(models.Model):
    user = models.IntegerField(default=0)
    message = models.CharField(max_length=200)
    has_read = models.BooleanField(default=False)
    add_time = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.user.username
