from django.shortcuts import render
from django.views.generic.base import View
from .models import Organization, CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .forms import UserAskForm
from django.http import HttpResponse
import json

# Create your views here.



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


# org_detail
class OrgDetailView(View):
    def get(self, request, org_id):
        org = Organization.objects.get(id=org_id)
        return render(request, 'org-detail-homepage.html', {
            'org': org,
        })
