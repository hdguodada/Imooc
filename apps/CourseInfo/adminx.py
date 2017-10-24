import xadmin
from xadmin import views
from .models import Course
from .models import Course_tag, Course_category, Course_style, Lesson, Video, CourseResource, BannerCourse


class LessonInline:
    model= Lesson
    extra = 0

class CourseResourceInline:
    model = CourseResource
    extra = 0


class CourseAdmin:
    list_display = ['name', 'organization']
    inlines = [LessonInline, CourseResourceInline]
    readonly_fields = ['click_num']

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs


class BannerCourseAdmin:
    list_display = ['name', 'organization']
    inlines = [LessonInline, CourseResourceInline]
    readonly_fields = ['click_num']

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs



class Course_categoryAdmin:
    list_display = ['name']


class Course_tagAdmin:
    list_display = ['name']


class Course_styleAdmin:
    list_display = ['name']


class LessonAdmin:
    list_display = ['name']


class VideoAdmin:
    list_display = ['name']


class CourseResourceAdmin:
    list_display = ['name']


xadmin.site.register(Course_tag, Course_tagAdmin)
xadmin.site.register(Course_category, Course_categoryAdmin)
xadmin.site.register(Course_style, Course_styleAdmin)
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
