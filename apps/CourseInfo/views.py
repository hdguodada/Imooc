from django.shortcuts import render
from django.views.generic.base import View
from .models import Course
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

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
        all_catogery = course.course_categories.all()
        return render(request, 'course-detail.html', {
            'course': course,
            'all_catogery': all_catogery,
            'current_page': current_page,
        })



class LessonView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)
        all_lessons = course.lesson_set.all()
        return render(request, 'course-video.html', {
            'course_id': course_id,
            'course': course,
            'all_lessons': all_lessons,
        })
