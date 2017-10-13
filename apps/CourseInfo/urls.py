from django.conf.urls import url
from .views import CourseView, CourseDetailView, TeacherView, TeacherDetailView


urlpatterns = [
    url(r'course_list/$', CourseView.as_view(), name='course_list'),
    url(r'course_detail/$',CourseDetailView.as_view(), name='course_detail'),
    url(r'teacher_list/$', TeacherView.as_view(), name='teacher_list'),
    url(r'teacher_detail/$', TeacherDetailView.as_view(), name='teacher_detail'),
]
