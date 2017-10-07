from django.shortcuts import render, reverse
from django.views.generic.base import View
from .forms import LoginForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')



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
