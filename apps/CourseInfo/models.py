from django.db import models
from OrganizationInfo.models import Organization

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=20)
    learn_time = models.IntegerField()
    image = models.ImageField(upload_to='course_image/%Y/%m')
    learn_num = models.IntegerField()
    organization = models.ForeignKey(Organization)

    def __str__(self):
        return self.name
