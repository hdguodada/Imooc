from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=(('male', 'man'), ('female', 'woman')), null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    mobilephone = models.IntegerField(unique=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m', default='default.png')

    class Meta:
        verbose_name = 'UserInfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def get_unread_nums(self):
        from operation.models import UserMessage
        return UserMessage.objects.filter(Q(user=self.id)|Q(user=0), has_read=False).count()



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


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题', null=True, blank=True)
    image = models.ImageField(upload_to='banner/%Y/%m', max_length=100, verbose_name='轮播图', null=True, blank=True)
    url = models.URLField(max_length=200, verbose_name='访问地址', null=True, blank=True)
    index = models.IntegerField(default=100, verbose_name='顺序')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间', null=True, blank=True)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


