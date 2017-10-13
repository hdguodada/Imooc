from django.db import models
from OrganizationInfo.models import Organization

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=20)
    learn_time = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to='course_image/%Y/%m')
    learn_num = models.IntegerField(default=0)
    fav_num = models.IntegerField(default=0)
    organization = models.ForeignKey(Organization)
    click_num = models.IntegerField(default=0)

    def __str__(self):
        return self.name
