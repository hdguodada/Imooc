import xadmin
from xadmin import views

from .models import UserAsk, UserCourse, UserFavorite, UserMessage, CourseComments


class UserAskAdmin:
    list_display = ['name', 'course_name']


class UserCourseAdmin:
    list_display = ['user', 'course']


class UserFavoriteAdmin:
    list_display = ['user', 'fav_id', 'fav_type']


class UserMessageAdmin:
    list_display = ['user', 'message', 'has_read']


class CourseCommentsAdmin:
    list_display = ['user', 'course', 'comments']



xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)

