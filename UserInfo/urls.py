from django.conf.urls import url
from .views import LoginView, LogoutView, RegisterView, ActiveView, ForgetPasswordView, ResetPassword
from .views import ModifyPwd, UserInfoView

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

]
