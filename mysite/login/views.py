from django.shortcuts import render, redirect
from . import forms, models
# Create your views here.


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None): #不允许重复登录
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

            if user.password == password:
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
    pass
    return render(request, 'login/register.html')


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出这一说
        return redirect('/login/')
    request.session.flush()
    return redirect('/login/')

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
