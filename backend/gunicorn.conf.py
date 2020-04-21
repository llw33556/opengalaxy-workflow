import sys
import os
import multiprocessing

proc_name = 'open-galaxy'
bind = "0.0.0.0:8000"
worker_class = 'sync'

# 工作进程数
workers = multiprocessing.cpu_count()
# 指定每个工作进程开启的线程数
threads = multiprocessing.cpu_count() * 2

# 启动方式
daemon = False

BASE_DIR = '/opt/open-galaxy/backend'
sys.path.append(BASE_DIR)

LOG_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
chdir = BASE_DIR

loglevel = 'debug'  # 日志级别，这个日志级别指的是错误日志的级别，而访问日志的级别无法设置
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
#
# # 访问日志文件
accesslog = '%s/access.log' %  (LOG_DIR)
# # 错误日志文件
errorlog = '%s/gunicorn_startup_info.log' %  (LOG_DIR)

pidfile = '%s/gunicorn.pid' % (LOG_DIR)

# 打到标准输出中
# accesslog = '-'
# errorlog = '-'