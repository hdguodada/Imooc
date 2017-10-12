import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import EmailVerifyRecord, UserProfile


class EmailVerifyRecordAdmin:
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
list_filter = ['code', 'email', 'send_type', 'send_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
