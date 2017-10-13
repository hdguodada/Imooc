from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

class CourseView(View):
    def get(self, request):
        return render(request, 'course-list.html')


class CourseDetailView(View):
    def get(self, request):
        return render(request, 'cours-detail.html')


class TeacherView(View):
    def get(self, request):
        return render(request, 'teacher-list.html')


class TeacherDetailView(View):
    def get(self, request):
        return render(request, 'teacher-detail.html')
