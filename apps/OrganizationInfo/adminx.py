import xadmin
from xadmin import views
from .models import Organization, CityDict, Teacher


class OrganizationAdmin:
    list_display = ['name']


class TeacherAdmin:
    list_display = [
        'name', 'organization'
    ]


class CityDictAdmin:
    list_display = [
        'name', 'desc'
    ]


xadmin.site.register(Organization, OrganizationAdmin)
xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
