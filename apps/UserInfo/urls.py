from django.conf.urls import url
from .views import LoginView, LogoutView, RegisterView, ActiveView, ForgetPasswordView, ResetPassword
from .views import ModifyPwd, UserInfoView, ImageUploadView, SendEmailCodeView, UpdateEmailView, MyCousreView
from .views import MyFavCourseView, MyMessage, MyFavOrgView, MyFavTeacherView

urlpatterns = [
    # login
    url(r'login/$', LoginView.as_view(),  name='login'),
    # logout
    url(r'logout/$', LogoutView.as_view(), name='logout'),
    # register
    url(r'register/$', RegisterView.as_view(),  name='register'),
    # active
    url(r'active/(?P<active_code>.*)/$', ActiveView.as_view(), name='active'),
    # forgetpassword
    url(r'forgetpassword/$', ForgetPasswordView.as_view(), name='forgetpassword'),
    # reset password
    url('reset_pwd/(?P<active_code>.*)/$', ResetPassword.as_view(), name='reset_pwd'),
    # modifypassword
    url('modifypassword/$', ModifyPwd.as_view(), name='modify'),
    # usercenter
    url('usercenter/$', UserInfoView.as_view(), name='usercenter'),
    # image upload
    url('image_upload/$', ImageUploadView.as_view(), name='image_upload'),
    # send email_code
    url('send_email_code/$', SendEmailCodeView.as_view(), name='send_email_code'),
    # update email
    url('update_email/$', UpdateEmailView.as_view(), name='update_email'),
    # mycourse
    url('my_course/$', MyCousreView.as_view(), name='my_course'),
    # myfavcourse
    url('my_fav/$', MyFavCourseView.as_view(), name='my_fav'),
    # myfavorg
    url('my_fav_org/$', MyFavOrgView.as_view(), name='my_fav_org'),
    # myfavteacher
    url('my_fav_teacher/$', MyFavTeacherView.as_view(), name='my_fav_teacher'),
    # mymessage
    url('my_message/$', MyMessage.as_view(), name='my_message'),
]
