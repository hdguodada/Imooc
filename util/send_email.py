from random import Random
import string

from django.core.mail import send_mail

from UserInfo.models import EmailVerifyRecord
from Imooc.settings import EMAIL_FROM


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == 'register':
        email_titile = 'welcome register'
        email_body = 'please touch link above:http://127.0.0.1:8000/user/active/{0}'.format(code)
        send_status = send_mail(email_titile, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
        pass
    if send_type == 'forget':
        email_titile = 'forget password'
        email_body = 'link: http://127.0.0.1:8000/user/reset_pwd/{0}'.format(code)
        send_status = send_mail(email_titile, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    if send_type == 'update_email':
        email_titile = 'update_email'
        email_body = 'your update_email code is {}.'.format(code)
        send_status = send_mail(email_titile, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def random_str(random_length=16):
    code =''
    chars = string.ascii_letters + str(string.digits)
    length = len(chars) - 1

    for i in range(random_length):
        code += chars[Random().randint(0, length)]
        pass
    return code
