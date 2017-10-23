from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Course
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from operation.models import UserFavorite

from random import choice

# Create your views here.

class CourseView(View):
    def get(self, request):
        # search

        # order
        all_courses = Course.objects.all()
        hot_courses = Course.objects.all().order_by('-click_num')[:3]
        if request.GET.get('sort') == 'hot':
            all_courses = all_courses.order_by('-fav_num')
        elif request.GET.get('sort') == 'students':
            all_courses = all_courses.order_by('learn_num')

        # fenye
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 15, request=request)
        courses = p.page(page)

        return render(request, 'course-list.html', {
            'all_courses': courses,
            'current_page': 'course',
            'hot_courses': hot_courses,
            'sort':request.GET.get('sort'),
        })


class CourseDetailView(View):
    def get(self, request, course_id):
        current_page = 'course'
        course = Course.objects.get(id=course_id)
        course.click_num += 1
        course.save()
        all_catogery = course.course_categories.all()
        relate_courses = []
        if all_catogery:
            for i in all_catogery:
                for j in i.course.all():
                    relate_courses.append(j)

        relate_course = []
        for i in range(2):
            relate_course.append(choice(relate_courses))

        has_course_faved = False
        has_org_faved = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_course_faved = True

            if UserFavorite.objects.filter(user=request.user, fav_id=course.organization.id, fav_type=2):
                has_org_faved = True

        return render(request, 'course-detail.html', {
            'course': course,
            'all_catogery': all_catogery,
            'current_page': current_page,
            'relate_course': relate_course,
            'has_org_faved': has_org_faved,
            'has_course_faved': has_course_faved,
        })



class LessonView(LoginRequiredMixin, View):
    login_url = 'user:login'
    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)
        course.learn_num += 1
        all_lessons = course.lesson_set.all()
        course_resource = course.courseresource_set.all()
        return render(request, 'course-video.html', {
            'course_id': course_id,
            'course': course,
            'all_lessons': all_lessons,
            'course_resource': course_resource,
        })


class CourseCommentsView(LoginRequiredMixin, View):
    login_url = 'user:login'
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        return render(request, 'course-comment.html', {
            'course': course,   
        })
