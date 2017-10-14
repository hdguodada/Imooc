from django.db import models

# Create your models here.


class Course_tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Course_category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
