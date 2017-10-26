import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import EmptyPage, PageNotAnInteger, Paginator

from CourseInfo.models import Course
from operation.models import UserFavorite

from .forms import UserAskForm
from .models import CityDict, Organization, Teacher

# Create your views here.


class AddFav(View):
    # fav_id: 收藏的机构，课程或者教师的id, fav_type:收藏类型，机构，课程或者教师
    def set_fav_num(self, fav_id, fav_type, num=1):
        if fav_type == 1:
            course = Course.objects.get(id=fav_id)
            # 课程收藏数+1
            course.fav_num += num
            course.save()
            pass
        if fav_type == 2:
            organization = Organization.objects.get(id=fav_id)
            # 机构收藏数+1
            organization.fav_num += num
            course.save()
            pass
        if fav_type == 3:
            teacher = Teacher.objects.get(id=fav_id)
            # 教师收藏数+1
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
            return HttpResponse(json.dumps(res), content_type='application/json')

        #判断是否已收藏
        exist_records = UserFavorite.objects.filter(user=request.user, fav_type=fav_type, fav_id=fav_id)
        if exist_records:
            # 已收藏的情况下点击按钮，则删除收藏
            exist_records.delete()
            res['status'] = 'success'
            res['msg'] ='收藏'
        else:
            if fav_type and fav_id:
                user_fav = UserFavorite()
                user_fav.user= request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type= int(fav_type)
                user_fav.save()
                self.set_fav_num(fav_id, fav_type, 1)

                res['status'] = 'success'
                res['msg']= '已收藏'
            else:
                res['status'] = 'fail'
                res['msg'] = '收藏出错'

        return HttpResponse(json.dumps(res), content_type='application/json')



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
        current_page = 'homepage'
        org = Organization.objects.get(id=org_id)
        all_course = org.course_set.all()[:3]
        all_teacher = org.teacher_set.all()[:3]
        teacher_and_first_course = {}
        for i in all_teacher:
            teacher_and_first_course[i] = i.course_set.all().order_by('-add_time')[0]
        # 验证是否已收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_type=2, fav_id=org_id):
                has_fav = True

        return render(request, 'org-detail-homepage.html', {
            'org': org,
            'all_course': all_course,
            'all_teacher': all_teacher,
            'org_id': org_id,
            'has_fav': has_fav,
            'teacher_and_first_course': teacher_and_first_course,
            'current_page': current_page,
        })


# org-detail-list
class OrgDetailCourseView(View):
    def get(self, request, org_id):
        current_page = 'course-list'
        org = Organization.objects.get(id=org_id)
        all_course = org.course_set.all()

        # 验证是否已收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_type=2, fav_id=org_id):
                has_fav = True

        # fenye
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_course, 8, request=request)
        courses = p.page(page)

        return render(request, 'org-detail-course.html', {
            'org_id': org_id,
            'org': org,
            'all_course': courses,
            'has_fav': has_fav,
            'current_page': current_page,
        })


class OrgDetalDescView(View):
    def get(self, request, org_id):
        current_page = 'desc'
        org = Organization.objects.get(id=org_id)
        # 验证是否已收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_type=2, fav_id=org_id):
                has_fav = True
        return render(request, 'org-detail-desc.html', {
            'org_id': org_id,
            'org': org,
            'current_page': current_page,
            'has_fav': has_fav,
        })



class OrgDetalTeacherView(View):
    def get(self, request, org_id):
        current_page = 'teacher'
        org = Organization.objects.get(id=org_id)
        all_teacher = org.teacher_set.all()
        # 验证是否已收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_type=2, fav_id=org_id):
                has_fav = True
        return render(request, 'org-detail-teachers.html', {
            'org_id': org_id,
            'org': org,
            'all_teacher': all_teacher,
            'current_page': current_page,
            'has_fav': has_fav,
        })



class TearcherView(View):
    def get(self, request):
        current_page = 'teacher'
        all_teachers = Teacher.objects.all()
        all_teacher_nums = all_teachers.count()
        hot_teachers = Teacher.objects.all().order_by('-fav_nums')[:3]
        fav_teachers = all_teachers.order_by('-fav_nums')
        sort = request.GET.get('sort')
        if sort == 'hot':
            all_teachers=fav_teachers
        # fenye
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_teachers, 8, request=request)
        teachers  = p.page(page)
        return render(request, 'teachers-list.html', {
            'all_teachers': teachers,
            'all_teacher_nums': all_teacher_nums,
            'hot_teachers': hot_teachers,
            'current_page': current_page,
            'sort': sort,
        })


class TeacherDetailView(View):
    def get(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Exception as e:
            return None
        teacher_course = teacher.course_set.all()
        has_teacher_faved = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=teacher.id, fav_type=3):
                has_teacher_faved = True
        has_org_faved = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=teacher.organization.id, fav_type=2):
                has_org_faved = True



        return render(request, 'teacher-detail.html', {
            'teacher': teacher,
            'teacher_course': teacher_course,
            'current_page': 'teacher',
            'has_teacher_faved': has_teacher_faved,
            'has_org_faved': has_org_faved,
        })

