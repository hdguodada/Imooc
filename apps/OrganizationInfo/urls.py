from django.conf.urls import url
from .views import OrgListView, UserAskView, OrgDetailView, OrgDetailCourseView


urlpatterns = [
    url(r'org_list/$', OrgListView.as_view(), name='org_list'),
    url(r'userask/$', UserAskView.as_view(), name='userask'),
    # detail-homepage
    url(r'org_detail_homepage/(?P<org_id>\d+)/$',  OrgDetailView.as_view(), name='org_detail'),
    # detail-course
    url(r'org_detail_course/(?P<org_id>\d+)/$', OrgDetailCourseView.as_view(), name='org_course'),
]
