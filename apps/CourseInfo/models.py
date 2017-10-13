from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=20)
    learn_time = models.IntegerField()
    image = models.ImageField(upload_to='course_image/%Y/%m')
    learn_num = models.IntegerField()
