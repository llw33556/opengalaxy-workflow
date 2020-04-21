# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms
from datetime import timedelta

platforms.C_FORCE_ROOT = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.update(
    CELERYBEAT_SCHEDULE={
        #工单审批提醒
        'workorder_remind_task': {
            'task': 'workflow.tasks.workorder_remind_task',
            'schedule':  timedelta(seconds=7200),
            'options': {
                'queue': 'task_b'
            }
        },
    }
)