from django.shortcuts import render, redirect
from . import forms, models
from django.conf import settings
import hashlib
import datetime

def index_test(request):
    return render(request, 'login/number-guessing-game-start.html')

def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session['user_name'] == 'yasin':
        print('111')
        from login.core import scheduler
        scheduler.start()
    # if request.session['user_name'] != 'yasin':

    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        # 前端验证
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except:
                message = '用户不存在!'
                return render(request, 'login/login.html', locals())
            if not user.has_confirmed:
                message = '该用户还未完成邮箱确认!'
                return render(request, 'login/login.html', locals())

            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = '密码不正确'
                return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = '请检查填写的内容'
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    massage = '用户名已存在!'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了!'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                code = make_confirm_string(new_user)
                send_email(email, code)
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html')


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出这一说
        return redirect('/login/')
    request.session.flush()
    return redirect('/login/')


def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求'
        return render(request, 'login/confirm.html', locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '邮箱确认成功，请使用账户登录!'
        return render(request, 'login/confirm.html', locals())


def hash_code(s, salt="mysite"):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def make_confirm_string(user: models.User) -> str:
    """ 生成确认码

    Parameters
    ----------
    user : models.ConfirmString
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user)
    return code


def send_email(email: str, code: str) -> None:
    """ 向目的邮箱地址发送确认码

    Parameters
    ----------
    email 目的邮箱地址
    code 确认码
    """
    from django.core.mail import EmailMultiAlternatives

    subject = f'来至白鬓少年: {settings.EMAIL_HOST} 的注册确认邮件'

    text_content = '''感谢注册django测试网站'''

    html_content = f'''
                    <p>感谢注册<a href="http://{'127.0.0.1:8000'}/confirm/?code={code}" target=blank>www.liujiangblog.com</a>,\
                    <p>请点击网站链接完成注册确认！</p>
                    <p>此链接有效期为{settings.CONFIRM_DAYS}'''

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

# def index(request):
#     # return HttpResponse('Hello 白鬓少年')
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # 将数据保存到数据库
#         models.User.objects.create(user=username, pwd=password)

#     # 从数据库中读取所有数据，注意缩进
#     user_list = models.User.objects.all()
#     return render(request, 'index.html', {'data': user_list})


# # user_list = []
# def index_back(request):
#     # return HttpResponse('Hello 白鬓少年')
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username, password)
#         temp = {'user': username, 'pwd': password}
#         user_list.append(temp)
#     return render(request, 'index.html', {'data': user_list})
