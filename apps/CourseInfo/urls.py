from django.conf.urls import url
from .views import CourseView, CourseDetailView, LessonView, CourseCommentsView, AddComments


urlpatterns = [
    url(r'course_list/$', CourseView.as_view(), name='course_list'),
    url(r'course_detail/(?P<course_id>.*)/$', CourseDetailView.as_view(), name='course_detail'),
    url(r'course_video/(?P<course_id>.*)/$', LessonView.as_view(), name='course_video'),
    url(r'course_comment/(?P<course_id>.*)/$', CourseCommentsView.as_view(), name='course_comment'),
    url(r'add_comment/$', AddComments.as_view(), name='add_comment'),
]
