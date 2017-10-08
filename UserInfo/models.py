from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=(('male', 'man'), ('female', 'woman')))
    address = models.CharField(max_length=100, null=True, blank=True)
    mobilephone = models.IntegerField(unique=True, null=True)

    class Meta:
        verbose_name = 'UserInfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
