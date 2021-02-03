from django.shortcuts import render
from django.shortcuts import HttpResponse
from login import models

# Create your views here.


def index(request):
    # return HttpResponse('Hello 白鬓少年')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 将数据保存到数据库
        models.UserInfo.objects.create(user=username, pwd=password)

    # 从数据库中读取所有数据，注意缩进
    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html', {'data': user_list})


# user_list = []
def index_back(request):
    # return HttpResponse('Hello 白鬓少年')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        temp = {'user': username, 'pwd': password}
        user_list.append(temp)
    return render(request, 'index.html', {'data': user_list})