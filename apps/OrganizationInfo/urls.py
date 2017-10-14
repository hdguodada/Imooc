from django.conf.urls import url
from .views import OrgListView


urlpatterns = [
    url(r'org_list/$', OrgListView.as_view(), name='org_list'),
]
