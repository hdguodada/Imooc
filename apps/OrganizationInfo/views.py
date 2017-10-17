from django.shortcuts import render
from django.views.generic.base import View

from .models import Organization, CityDict, Teacher
from CourseInfo.models import Course

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .forms import UserAskForm
from django.http import HttpResponse
from operation.models import UserFavorite
import json

# Create your views here.


class AddFav(View):
    def set_fav_num(self, fav_id, fav_type, num=1):
        if fav_type == 1:
            course = Course.objects.get(id=fav_id)
            course.fav_num += num
            course.save()
            pass
        if fav_type == 2:
            organization = Organization.objects.get(id=fav_id)
            organization.fav_num += num
            course.save()
            pass
        if fav_type == 3:
            teacher = Teacher.objects.get(id=fav_id)
            teacher.fav_num += num
            teacher.save()
            pass

    def post(self, request):
        fav_type = request.POST.get('fav_type')
        fav_id = request.POST.get('fav_id')
        res = dict()
        if not request.user.is_authenticated():
            res['status'] = 'fail'
            res['msg'] = '用户未登录'
            return HttpResponse()
        else:
            user_fav = UserFavorite()
            user_fav.user= user
            user_fav.fav_id = int(fav_id)
            user_fav.fav_type= int(fav_type)
            user_fav.save()
        except Exception as e:
            return null


class OrgListView(View):
    def get(self, request):
        org_list = Organization.objects.all()
        all_city = CityDict.objects.all()
        hot_org = Organization.objects.all().order_by('-fav_nums')[:3]
        category = request.GET.get('ct', '')
        city_id = request.GET.get('city', '')
        if category:
            org_list = Organization.objects.filter(category=request.GET.get('ct'))
        if city_id:
            org_list = Organization.objects.filter(city=request.GET.get('city'))


        org_num = org_list.count()

        # fenye
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(org_list, 10, request=request)
        org = p.page(page)

        return render(request, 'org-list.html', {
            'current_page': 'org',
            'org_list': org,
            'all_city': all_city,
            'city_id': city_id,
            'category': category,
            'org_num': org_num,
            'hot_org': hot_org,
        })



class UserAskView(View):
    def post(self, request):
        user_ask_form = UserAskForm(request.POST)
        res = dict()
        if user_ask_form.is_valid():
            user_ask_form.save(commit=True)
            res['status'] = 'success'
            return HttpResponse(json.dumps(res), content_type='application/json')
        else:
            res['status'] = 'fail'
            res['msg'] = 'wrong'
            return HttpResponse(json.dumps(res), content_type='application/json')


# org_homepage
class OrgDetailView(View):
    def get(self, request, org_id):
        org = Organization.objects.get(id=org_id)
        all_course = org.course_set.all()[:3]
        all_teacher = org.teacher_set.all()[:3]

        # 验证是否已收藏




        return render(request, 'org-detail-homepage.html', {
            'org': org,
            'all_course': all_course,
            'all_teacher': all_teacher,
            'org_id': org_id,
        })


# org-detail-list
class OrgDetailCourseView(View):
    def get(self, request, org_id):
        return render(request, 'org-detail-course.html', {
            'org_id': org_id,
        })
