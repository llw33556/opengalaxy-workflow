if [ `ps -ef|grep celery|grep task_a,task_b|grep -v grep|wc -l` -gt 0 ];then
    ps -ef|grep celery|grep task_a,task_b|awk '{print $2}'|grep -v grep|xargs kill -9
    test -f  backend/logs/celery/celery_task.pid && rm -f backend/logs/celery/celery_task.pid
fi

if [ `ps -ef|grep celery|grep beat|grep -v grep|wc -l` -gt 0 ];then
    ps -ef|grep celery|grep beat|awk '{print $2}'|grep -v grep|xargs kill -9
    test -f  backend/logs/celery/celery_beat.pid && rm -f backend/logs/celery/celery_beat.pid
fi
if [ `ps -ef|grep celery|grep flower|grep -v grep|wc -l` -gt 0 ];then
    ps -ef|grep celery|grep flower|awk '{print $2}'|grep -v grep|xargs kill -9
    test -f  backend/logs/celery/celery_flower.pid && rm -f backend/logs/celery/celery_flower.pid
fi
source env/bin/activate && cd backend && nohup  celery worker -A project --loglevel=info -Q task_a,task_b -c 16 --loglevel=info --pidfile=logs/celery/celery_task.pid &>logs/celery/celery_task.log 2>&1 &
source env/bin/activate && cd backend && nohup celery beat -A project --loglevel=info --pidfile=logs/celery/celery_beat.pid &>logs/celery/celery_beat.log 2>&1 &
source env/bin/activate && cd backend && nohup  celery flower -A project --loglevel=info --pidfile=logs/celery/celery_flower.pid &>logs/celery/celery_flower.log 2>&1 &