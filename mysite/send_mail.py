import os
from django.core.mail import send_mail


os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    send_mail(
        'Django测试邮件',
        '心有猛虎，细嗅蔷薇',
        '18842661643@163.com',
        ['yasinliu615@gmail.com']
    )