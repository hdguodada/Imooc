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


class UserMessage(models.Model):
    user = models.ForeignKey(UserProfile)
    message = models.CharField(max_length=500, verbose_name='message')
    has_read = models.BooleanField(default=False)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name_plural = 'usermessage'
        pass
    def __str__(self):
        return self.message


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    send_type = models.CharField(max_length=18, choices=(('register', 'email'), ('forget', 'modifypassword'), ('update_email', 'modify_email')))
    has_user = models.BooleanField(default=False)
    send_time = models.DateTimeField(default=datetime.now)
    class Meta:
        verbose_name_plural = 'emailcode'
        pass

    def __str__(self):
        return self.send_type
