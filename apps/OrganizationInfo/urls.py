from django.conf.urls import url
from .views import OrgListView, UserAskView, OrgDetailView


urlpatterns = [
    url(r'org_list/$', OrgListView.as_view(), name='org_list'),
    url(r'userask/$', UserAskView.as_view(), name='userask'),
    # detail
    url(r'org_detail/(?P<org_id>\d+)/$',  OrgDetailView.as_view(), name='org_detail')
]
