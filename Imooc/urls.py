"""Imooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from UserInfo.views import IndexView
from django.views.static import serve
from Imooc.settings import MEDIA_ROOT
import xadmin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    # 首页
    url(r'^$', IndexView.as_view(), name='index'),
    # 用户中心
    url(r'^user/', include('UserInfo.urls', namespace='user')),
    # 验证码
    url(r'captcha/', include('captcha.urls')),
    # media url
    url(r'media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
    # course
    url(r'^course/', include('CourseInfo.urls', namespace='course')),
    #org
    url(r'^org/', include('OrganizationInfo.urls', namespace='org')),

]

# 全局404与500
handler404 = 'user.views.page_not_found'
handler500 = 'user.views.page_error'


if settings.DEBUG:
    pass
else:
    # 项目部署上线时使用
    from Imooc.settings import STATIC_ROOT
    # 配置静态文件访问处理
    urlpatterns.append(url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}))
