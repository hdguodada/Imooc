from django.conf.urls import url
from .views import OrgListView, UserAskView, OrgDetailView, OrgDetailCourseView, AddFav
from .views import OrgDetalDescView, OrgDetalTeacherView, TearcherView


urlpatterns = [
    url(r'org_list/$', OrgListView.as_view(), name='org_list'),
    url(r'userask/$', UserAskView.as_view(), name='userask'),
    # detail-homepage
    url(r'org_detail_homepage/(?P<org_id>\d+)/$',  OrgDetailView.as_view(), name='org_detail'),
    # detail-course
    url(r'org_detail_course/(?P<org_id>\d+)/$', OrgDetailCourseView.as_view(), name='org_course'),
    # add_fav
    url(r'add_fav/$', AddFav.as_view(), name='add_fav'),
    # org-detail-desc
    url(r'org_detail_desc/(?P<org_id>\d+)/$', OrgDetalDescView.as_view(), name='org_desc'),
    # org-detail-teacher
    url(r'org_detail_teacher/(?P<org_id>\d+)/$', OrgDetalTeacherView.as_view(), name='org_teacher'),
    # Teacher
    url(r'teacher_list/$', TearcherView.as_view(), name='teacher_list'),
]
