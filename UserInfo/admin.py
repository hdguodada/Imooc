from django.contrib import admin
from .models import UserProfile, UserMessage, EmailVerifyRecord
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'gender']
    pass


class UserMessageAdmin(admin.ModelAdmin):
    pass


class EmailAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserMessage, UserMessageAdmin)
admin.site.register(EmailVerifyRecord, EmailAdmin)
