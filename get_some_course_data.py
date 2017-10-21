import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Imooc.settings')
from Imooc.settings import MEDIA_ROOT

import django
django.setup()

import requests
from bs4 import BeautifulSoup

from CourseInfo.models import Course, Course_tag, Course_category, Course_style, Lesson, Video

from urllib.parse import urljoin

import time


host_url = 'http://www.imooc.com'


def get_course_category():
    res = requests.get('http://www.imooc.com/course/list?page=1')
    soup = BeautifulSoup(res.text, 'lxml')
    category_list = soup.select('.bd')[1].find_all('li')[1:]
    try:
        for i in category_list:
            print(i.text.strip('/n'))
            category_name = i.text.strip('/n')
            Course_category.objects.get_or_create(name=category_name)
            print(category_name + 'created')
    except Exception as e:
        print('jinggao')


def get_course_list():
    for i in range(1, 32):
        res = requests.get('http://www.imooc.com/course/list?page={0}'.format(i))
        soup = BeautifulSoup(res.text, 'lxml')
        course_list = soup.select('.course-card-container')
        for course in course_list:
            course_name = course.h3.text
            course_url = urljoin(host_url, course.a.attrs['href'])
            try:
                course_img_url = 'http:' +  course.img.attrs['src']
                print(course_img_url)
                with open(os.path.join(MEDIA_ROOT, 'course_image/2017/10/{0}.png'.format(course_name)), 'wb') as f:
                    f.write(requests.get(course_img_url).content)
            except Exception as e:
                print('image save fail')
            course_category_list = course.find_all('label')
            course_degree = course.span.text
            course_desc = course.p.text
            try:
                cs = Course()
                cs.name = course_name
                cs.desc = course_desc
                cs.degree = course_degree
                cs.detail = course_url
                cs.image = 'course/2017/10{0}.png'.format(course_name)
                cs.save()
                print('course save sucess')
            except Exception as e:
                print('fail')

            for course_category in course_category_list:
                try:
                    category = Course_category.objects.get_or_create(name=course_category.text)
                    category[0].course.add(cs)
                    print('course_category save sucess')
                except Exception as e:
                    print('course_category save fail')


            print('time sleep 10 second')



def get_lesson_data():
    all_courses = Course.objects.all()
    for course in all_courses:
        if course.detail.startswith('http'):
            res = requests.get(course.detail)
            soup = BeautifulSoup(res.text, 'lxml')
            course.you_need_know = soup.find_all('dd')[0].text
            course.teacher_tell_you = soup.find_all('dd')[0].text
            course.save()
            for lesson in soup.select('.chapter'):
                # 章节名
                lesson_name = lesson.strong.text.strip().split('\r')[0]
                # 所属课程
                lesson_course = course
                Lesson.objects.get_or_create(name=lesson_name, course=lesson_course)
                print(lesson_name + 'save sucess')
                for video in lesson.find_all('a'):
                    video_name = video.text.strip().split('\r')[0]
                    video_lesson = Lesson.objects.get(name=lesson_name, course=lesson_course)
                    # 每节时长
                    video_time = video.text.strip().split('\r')[1].strip()
                    aa = Video.objects.get_or_create(name=video_name, lesson=video_lesson)
                    aa[0].video_time = video_time
                    aa[0].save()
                    print(video_name + 'save sucess')

            


if __name__ == '__main__':
    get_lesson_data()
