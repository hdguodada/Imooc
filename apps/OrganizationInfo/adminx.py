import xadmin
from xadmin import views
from .models import Organization, CityDict, Teacher


class OrganizationAdmin:
    list_display = ['name']
    # Course的外键指向这里，在添加Course时，选择机构采用下拉的方式，如果数据过大，会影响页面，也影响操作，
    # 采用下拉的方式
    relfield_style = 'fk-ajax'


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
