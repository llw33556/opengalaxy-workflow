---

## Description

This is an example of demo application that uses **django & django rest framework** as a backend and **vue.js** as a frontend.

## Environment

```
Centos 6/7
Python 3.6.1-6
mysql-server 5.6.21
node 9.4.0
Django==2.1.4
djangorestframework==3.9.0
```

## How to run

Clone the repository:

```zsh
➜ git clone git@gitlab.opengalaxy.com:devops/django-vue-demo.git
```

Create and activate virtualenv:

```zsh
➜  virtualenv -p python3 env
➜  source env/bin/activate
```

Run scripts from Makefile that install all dependencies, run migrations and start dev server.

```zsh
(env) ➜  mysql -uroot -p -e "create database demo default charset utf8;"
(env) ➜  cp backend/.env_example backend/.env     #修改后端配置
(env) ➜  make init
(env) ➜  make build-prod
```

Nginx config

```
dev
  use  opengalaxy.tx.cc.conf

prod
  use  opengalaxy.tx.cn.conf

```

OpenGalaxy Start

```zsh
(env) ➜  make build-prod    #dev
(env) ➜  make start    #dev
(env) ➜  make restart-celery    #dev
```

We are done.

dev

- ALL:      http://opengalaxy.tx.cc/
- Frontend: http://opengalaxy.tx.cc:9527/
- Backend: http://opengalaxy.tx.cc:8002/

prod

- Frontend: http://opengalaxy.tx.cn/
- Backend: http://opengalaxy.tx.cn/api/
- Xadmin: http://opengalaxy.tx.cn/xadmin/
- API Docs: http://opengalaxy.tx.cn/docs/

默认管理员账号：admin   密码：1password1
