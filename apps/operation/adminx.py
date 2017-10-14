import xadmin
from xadmin import views
from .models import Course_category, Course_tag


class Course_categoryAdmin:
    list_display = ['name']


class Course_tagAdmin:
    list_display = ['name']


xadmin.site.register(Course_tag, Course_tagAdmin)
xadmin.site.register(Course_category, Course_categoryAdmin)
