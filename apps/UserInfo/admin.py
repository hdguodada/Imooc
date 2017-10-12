from django.contrib import admin
from .models import UserProfile, UserMessage, EmailVerifyRecord
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'gender']
    pass


class UserMessageAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'has_read', 'add_time'
    ]


class EmailAdmin(admin.ModelAdmin):
    list_display = [
        'code', 'email', 'send_type', 'has_user', 'send_time'
    ]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserMessage, UserMessageAdmin)
admin.site.register(EmailVerifyRecord, EmailAdmin)
