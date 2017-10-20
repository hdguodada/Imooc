from django.conf.urls import url
from .views import CourseView, CourseDetailView, LessonView


urlpatterns = [
    url(r'course_list/$', CourseView.as_view(), name='course_list'),
    url(r'course_detail/(?P<course_id>.*)/$', CourseDetailView.as_view(), name='course_detail'),
    url(r'course_video/(?P<course_id>.*)/$', LessonView.as_view(), name='course_video'),
]
