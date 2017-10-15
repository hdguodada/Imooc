import os
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'Imooc.settings'
)

import django
django.setup()
from Imooc.settings import MEDIA_ROOT

import requests
from bs4 import BeautifulSoup
from random import randint

from OrganizationInfo.models import Organization


response = requests.get('http://college.gaokao.com/schlist/p1/')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')

for school in soup.select('.scores_List > dl'):
    school_name = school.find_all('a')[1].text
    school_address =  school.find_all('li')[0].text.split('：')[1]
    school_image_url = school.find_all('a')[0].img['src']
    with open(os.path.join(MEDIA_ROOT, 'organization/2017/10/{0}.png').format(school_name), 'wb') as f:
        f.write(requests.get(school_image_url).content)
        pass
    school_student = randint(100, 500)
    Organization.objects.get_or_create(name=school_name, address=school_address, image='organization/2017/10/{0}.png'.format(school_name))
