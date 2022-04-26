"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('polls/', include('polls.urls')),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('capthca/', include('captcha.urls')),
    path('confirm/', views.user_confirm),
]

# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
# from django_apscheduler.jobstores import register_job, register_events, DjangoJobStore
# import time
#
# # 实例化调度器
# scheduler = BackgroundScheduler()
# # 调度器使用DjangoJobStore()
# scheduler.add_jobstore(DjangoJobStore(), "default")
# @register_job(scheduler, 'interval', seconds=3, replace_existing=True)
# def job1():
#     # 具体要执行的代码
#     print('{} 任务运行成功！{}'.format('na', time.strftime("%Y-%m-%d %H:%M:%S")))
#     print('job2')
# register_events(scheduler)
# scheduler.start()
# print('Scheduler started!')

# from apscheduler.schedulers.background import BackgroundScheduler
# from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
#
# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), "default")
#
#
# # 时间间隔3秒钟打印一次当前的时间
# @register_job(scheduler, "interval", seconds=3, id='test_job', replace_existing=True)
# def test_job():
#     print("我是apscheduler任务")
# # per-execution monitoring, call register_events on your scheduler
# register_events(scheduler)
# scheduler.start()
# print("Scheduler started!")
