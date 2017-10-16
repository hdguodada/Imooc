import xadmin
from xadmin import views
from .models import Course
from .models import Course_tag, Course_category, Course_style


class CourseAdmin:
    list_display = ['name', 'organization']

class Course_categoryAdmin:
    list_display = ['name']


class Course_tagAdmin:
    list_display = ['name']


class Course_styleAdmin:
    list_display = ['name']


xadmin.site.register(Course_tag, Course_tagAdmin)
xadmin.site.register(Course_category, Course_categoryAdmin)
xadmin.site.register(Course_style, Course_styleAdmin)

xadmin.site.register(Course, CourseAdmin)
