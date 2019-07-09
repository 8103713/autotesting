#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ------------------------------------------
# @Time     : 2019/2/25 12:45
# @Author   : liuss
# @Site     : 
# @File     : time_task.py
# @Software : PyCharm Community Edition
# @Version  :
#--------------------------------------------

from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import datetime,os

"""执行多个定时任务
    #tasks=[[func,trigger,time,id],[func,trigger,time,id],[func,trigger,time,id],]
    #trigger:interval（间隔）,cron(指定时间段定时),date(执行一次)
    #time:
        # interval:hours=3/minutes=3/seconds=3(每隔3小时/3分钟/3秒执行)
        # cron:hour =19 ,minute =23(每天的19：23 分执行任务)
        # date:run_date='2018-04-05 07:48:05'
"""
def excTasks(tasks):
    job_defaults = { 'max_instances': 2 }
    scheduler = BlockingScheduler(job_defaults=job_defaults)
    if tasks is not None:
        if isinstance(tasks[0],list):
            for task in tasks:
                addTask(scheduler,task)
        else:
            addTask(scheduler,tasks)
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.pause()

def addTask(scheduler,task):
    func=task[0]
    trigger=task[1]
    time=task[2]
    id=task[3]
    if trigger=="interval":
        times=time.split("=")
        time_unit=times[0]
        time_interval=int(times[1])
        if time_unit=="hour":
            scheduler.add_job(func=func, args=[id,], trigger=trigger, hours=time_interval)
        elif time_unit=="minute":
            scheduler.add_job(func=func, args=[id,], trigger=trigger, minutes=time_interval)
        elif time_unit=="second":
            scheduler.add_job(func=func, args=[id,], trigger=trigger, seconds=time_interval)
    elif trigger=="date":
        times=time.split("=")
        scheduler.add_job(func=func, args=[id,], trigger=trigger, run_date=times[1])
    elif trigger=="cron":
        term="func=func, args=[id,], trigger=trigger, "
        times=time.split(",")
        for i in times:
            term=term+i+","
        scheduler.add_job(term[:-1])
"""
#trigger:interval（间隔）,cron(指定时间段定时),date(执行一次)
#time:
    # interval:hours=3/minutes=3/seconds=3(每隔3小时/3分钟/3秒执行)
    # cron:hour =19 ,minute =23(每天的19：23 分执行任务)
    # date:run_date='2018-04-05 07:48:05'
def excTask(func,trigger,time,id):
    job_defaults = { 'max_instances': 5 }
    scheduler = BlockingScheduler(job_defaults=job_defaults)
    if trigger=="interval":
        times=time.split("=")
        time_unit=times[0]
        time_interval=int(times[1])
        if time_unit=="hour":
            scheduler.add_job(func=func, args=[id,], trigger=trigger, hours=time_interval)
        elif time_unit=="minute":
            scheduler.add_job(func=func, args=[id,], trigger=trigger, minutes=time_interval)
        elif time_unit=="second":
            scheduler.add_job(func=func, args=[id,], trigger=trigger, seconds=time_interval)
    elif trigger=="date":
        times=time.split("=")
        scheduler.add_job(func=func, args=[id,], trigger=trigger, run_date=times[1])
    elif trigger=="cron":
        term="func=func, args=[id,], trigger=trigger, "
        times=time.split(",")
        for i in times:
            term=term+i+","
        scheduler.add_job(term[:-1])
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler.start()
"""
def my_listener(event):
    if event.exception:
        print(datetime.datetime.now(),"--->","fail")
        print (event)
        print('====================================================')
    else:
        print(datetime.datetime.now(),"--->","pass")
        print('====================================================')