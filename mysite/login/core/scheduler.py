import logging
import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from django_apscheduler.jobstores import register_job, register_events
from django.conf import settings

scheduler = BackgroundScheduler(settings.SCHEDULER_CONFG)

def job1(name):
    # 具体要执行的代码
    print('{} 任务运行成功！{}'.format(name, time.strftime("%Y-%m-%d %H:%M:%S")))

def job2(name):
    # 具体要执行的代码
    print('{} 任务运行成功！{}'.format(name, time.strftime("%Y-%m-%d %H:%M:%S")))


def start():
    # if settings.DEBUG:
    #     logging.basicConfig()
    #     logging.getLogger('apscheduler').setLevel(logging.DEBUG)
    scheduler.add_job(job1, "cron", second='05', args=['奥特曼'], id='job1', replace_existing=True)
    scheduler.add_job(job2, 'cron', second='35', args=['燕麦'], id='job2', replace_existing=True)
    # scheduler.add_job(job1, "interval", seconds=3, args=['沈复'], id='job1', replace_existing=True)
    # scheduler.add_job(job2, "interval", seconds=5, args=['黄桃'], id='job2', replace_existing=True)

    register_events(scheduler)
    scheduler.start()
