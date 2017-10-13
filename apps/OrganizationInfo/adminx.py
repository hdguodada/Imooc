import xadmin
from xadmin import views
from .models import Organization


class OrganizationAdmin:
    list_display = ['name']



xadmin.site.register(Organization, OrganizationAdmin)
