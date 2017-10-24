from django.shortcuts import render, reverse
from django.views.generic.base import View

from .forms import LoginForm, RegisterForm, ForgetPasswordForm, ModifyPasswordForm, ImageForm
from .forms import UserInfoForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, EmailVerifyRecord
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from util.send_email import send_register_email
import datetime
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from operation.models import UserCourse, UserFavorite, UserMessage
from CourseInfo.models import Course, BannerCourse
from OrganizationInfo.models import Organization, Teacher
import json

# Create your views here.

# email authenticate
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class IndexView(View):
    def get(self, request):
        banner_course = BannerCourse.objects.all()[:5]
        return render(request, 'index.html', {
            'banner_course': banner_course,
        })



class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, 'login.html', {
                        'msg': 'the user is not active',
                    })
            else:
                return render(request, 'login.html', {
                    'msg': 'the password is wrong',
                })
            pass
        return render(request, 'login.html', {
            'form_errors': login_form.errors,
        })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


# register
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {
            'register_form': register_form,
        })

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            if UserProfile.objects.filter(email=email):
                return render(request, 'register.html', {
                    'msg': 'the username has joined' })
            else:
                user = UserProfile()
                user.username = email
                user.email = email
                user.password = make_password(password)
                user.is_active = False
                user.save()

                message = UserMessage()
                message.user = user
                message.message = 'thank you for your register, please touch the link'
                message.save()
                send_register_email(email, 'register')
                return render(request, 'send_success.html')
            pass
        return render(request, 'register.html', {'register_form': register_form})


class ActiveView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                return render(request, 'login.html')
            return render(request, 'active_fail.html')



# forget password
class ForgetPasswordView(View):
    def get(self, request):
        forget_form = ForgetPasswordForm()
        return render(request, 'forgetpwd.html', {
            'forget_form': forget_form,
        })

    def post(self, request):
        forget_form = ForgetPasswordForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email')
            try:
                user = UserProfile.objects.get(email=email)
            except Exception as e:
                return render(request, 'forgetpwd.html',{
                    'forget_form':forget_form,
                    'msg': 'yonghubucunzai ',
                })
            message = UserMessage()
            message.user = user
            message.save()
            send_register_email(email, 'forget')
            return HttpResponse('please look your Email:{0}'.format(email))
        else:
            return render(request, 'forgetpwd.html', {
                'forget_form':forget_form,
            })



class ResetPassword(View):
    def get(self, request, active_code):
        try:
            record = EmailVerifyRecord.objects.get(code=active_code)
        except Exception as e:
            return HttpResponse('lianjie bu cun zai')

        if ((timezone.now() - record.send_time).total_seconds()) > 15*60:
            return HttpResponse('lianjie shi xiao')
        else:
            return render(request, 'password_reset.html', {
                'email': record.email,
            })


class ModifyPwd(View):
    def post(self, request):
        modify_form = ModifyPasswordForm(request.POST)
        if modify_form.is_valid():
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            email = request.POST.get('email')
            if password1 == password2:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(password1)
                user.save()
                return render(request, 'login.html')
            return render(request, 'password_reset.html', {
                'email': email,
                'msg': 'the password is diff',
            })


# UserInfo
class UserInfoView(LoginRequiredMixin, View):
    login_url = 'user:login'
    def get(self, request):
        current_page = 'userinfo'
        return render(request, 'usercenter-info.html', {
            'current_page': current_page,
        })

    def post(self, request):
        print('1')
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        res = dict()
        if user_info_form.is_valid():
            print('2')
            user_info_form.save()
            res['status'] = 'success'
        else:
            print('3')
            res = user_info_form.errors
            for k,  v in res.items():
                print(k)
                print(v)
        return HttpResponse(json.dumps(res), content_type='application/json')





# 个人头像
class ImageUploadView(View):
    def post(self, request):
        image_form = ImageForm(request.POST, request.FILES, instance=request.user)
        res = dict()
        if image_form.is_valid():
            image_form.save()
            res['status'] = 'success'
            res['msg'] = '头像修改成功'
        else:
            res['status'] = 'Fail'
            res['msg'] = '头像修改失败'
        return HttpResponse(json.dumps(res), content_type='application/json')


# 个人中心更新密码
class UpdatePwdView(View):
    def post(self, request):
        modify_form = ModifyPasswordForm(request.POST)
        res = dict()
        if modify_form.is_valid():
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            user = request.user
            if password1 != password2:
                res['status'] = 'fail'
                res['msg'] = '两次密码不一样'
                return HttpResponse(json.dumps(res), content_type='application/json')
            res['status'] = 'success'
            res['msg'] = '密码修改成功'
            return HttpResponse(json.dumps(res), content_type='application/json')
        res = modify_form.errors
        return HttpResponse(json.dumps(res), content_type='application/json')


# userinfo modify email - send email
class SendEmailCodeView(View):
    def get(self, request):
        res = dict()
        email = request.GET.get('email')
        if UserProfile.objects.filter(email=email):
            res['email'] = 'the email has exist'
            return HttpResponse(json.dumps(res), content_type='application/json')
        send_register_email(email, 'update_email')
        message = UserMessage()
        message.user = request.user
        message.message = 'update email in userinfo'
        message.save()
        res['status'] = 'success'
        res['msg'] = 'send success'
        return HttpResponse(json.dumps(res), content_type='application/json')



# modify email in userinfo
class UpdateEmailView(View):
    def post(self, request):
        email = request.POST.get('email')
        code = request.POST.get('code')
        res = dict()
        try:
            email_record = EmailVerifyRecord.objects.get(code=code)
        except Exception as e:
            res['status'] = 'fail'
            res['msg'] = 'the code is wrong'
            return HttpResponse(json.dumps(res), content_type='application/json')

        has_expired = ((timezone.now() - email_record.send_time).total_seconds()) > 15*60
        if not has_expired:
            user = request.user
            user.email = email
            user.save()
            res['status'] = 'success'
            res['msg'] = 'update success'
            return HttpResponse(json.dumps(res), content_type='application/json')
        else:
            res['status'] = 'fail'
            res['msg'] = 'the code has expired'
            return HttpResponse(json.dumps(res), content_type='application/json')



class MyCousreView(View):
    def get(self, request):
        current_page = 'mycourse'
        user_course = UserCourse.objects.filter(user=request.user)
        course_ids = [course.course.id for course in user_course]
        all_courses = Course.objects.filter(id__in=course_ids)

        return render(request, 'usercenter-mycourse.html', {
            'all_courses': all_courses,
            'current_page': current_page,
        })


class MyFavCourseView(View):
    def get(self, request):
        user = request.user
        course_fav = UserFavorite.objects.filter(user=user, fav_type=1)
        fav_ids = [course.fav_id for course in course_fav]
        fav_courses = Course.objects.filter(id__in=fav_ids)
        return render(request, 'usercenter-fav-course.html',{
            'fav_courses': fav_courses,
        })


class MyFavOrgView(View):
    def get(self, request):
        user = request.user
        org_fav = UserFavorite.objects.filter(user=user, fav_type=2)
        fav_ids = [org.fav_id for org in org_fav]
        fav_orgs = Organization.objects.filter(id__in=fav_ids)
        return render(request, 'usercenter-fav-org.html', {
            'fav_orgs': fav_orgs,
        })


class MyFavTeacherView(View):
    def get(self, request):
        user = request.user
        teacher_fav = UserFavorite.objects.filter(user=request.user, fav_type=3)
        fav_ids = [teacher.fav_id for teacher in teacher_fav]
        fav_teachers = Teacher.objects.filter(id__in=fav_ids)
        return render(request, 'usercenter-fav-teacher.html', {
            'fav_teachers': fav_teachers,
        })


class MyMessage(LoginRequiredMixin, View):
    login_url = 'user:login'
    def get(self, request):
        user = request.user
        user_message = UserMessage.objects.filter(user=user.id)
        return render(request, 'usercenter-message.html', {
            'user_message': user_message,
        })



