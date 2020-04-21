init:
	cd frontend && cnpm install
	source env/bin/activate && pip install -r backend/requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
	source env/bin/activate && python backend/manage.py makemigrations && python backend/manage.py migrate
	source env/bin/activate && python backend/manage.py init_users
	source env/bin/activate && python backend/manage.py init_mdjcelery
	source env/bin/activate && python backend/manage.py init_workflow
	source env/bin/activate && python backend/manage.py collectstatic --noinput

migrate:
	source env/bin/activate && python backend/manage.py makemigrations && python backend/manage.py migrate

dev:
	npm run --prefix frontend dev & (source env/bin/activate && python backend/manage.py runserver)
	/bin/sh restart_celery.sh

start:
	test ! -f backend/logs/gunicorn.pid && source env/bin/activate && (nohup gunicorn -c backend/gunicorn.conf.py project.wsgi &) || echo 'gunicorn running'
	echo "`date` start" >> backend/logs/restart.log

stop:
	test -f backend/logs/gunicorn.pid && source env/bin/activate && kill -9 `cat backend/logs/gunicorn.pid`  || echo 'gunicorn closed'
	rm -f backend/logs/gunicorn.pid
	echo "`date` stop" >> backend/logs/restart.log

restart:
	test -f backend/logs/gunicorn.pid && source env/bin/activate && kill -9 `cat backend/logs/gunicorn.pid`  || echo 'gunicorn closed'
	rm -f backend/logs/gunicorn.pid
	test ! -f backend/logs/gunicorn.pid && source env/bin/activate && (nohup gunicorn -c backend/gunicorn.conf.py project.wsgi &)  || echo 'gunicorn running'
	echo "`date` restart" >> backend/logs/restart.log

build-prod:
	npm run --prefix frontend  build:prod
	source env/bin/activate && python backend/manage.py collectstatic --noinput

build-test:
	npm run --prefix frontend  build:test
	source env/bin/activate && python backend/manage.py collectstatic --noinput

restart-celery:
	/bin/sh restart_celery.sh
