import xadmin
from xadmin import views
from .models import Course


class CourseAdmin:
    list_display = ['name', 'organization']


xadmin.site.register(Course, CourseAdmin)
