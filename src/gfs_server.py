# -*- coding: utf-8 -*-
from lib.server.filesystem_server import operator
import threading
import configparser
import os,sys

MAINPATH = sys.path[1]
cf = configparser.ConfigParser()
cf.read(os.path.join(os.path.join(MAINPATH, 'config'), 'server'), encoding='utf-8')

FILEPATHLIST = [d for d in cf.get('server', 'filedir').split('|')]
print(FILEPATHLIST)
def func1(time):
    print("定时任务启动。。。。。。")
    M = operator(FILEPATHLIST)
    print("更新数据库：{}".format([filename[0] for filename in M.datalist]))
    M.upDateDb()
    print("数据库更新完成，开始清理垃圾数据。。。")
    M.clearData()
    print("任务结束。")
    global timer
    timer = threading.Timer(time, func1, args=[time])
    timer.start()
#func1(10)
