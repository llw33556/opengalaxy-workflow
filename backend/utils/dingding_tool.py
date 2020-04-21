# -*- coding: utf-8 -*-
import requests
import json
from django.conf import settings
from .util import get_request_client
from workflow.models import AuditStep

import logging
logger = logging.getLogger('views')

class DingTalk(object):
    def __init__(self):
        self.agent_id = settings.DINGDING_AGENTID
        self.app_secret = settings.DINGDING_SECRET
        self.app_key = settings.DINGDING_APPKEY
        self.corp_id = settings.DINGDING_CORPID
        self.request_session = get_request_client()
        self.access_token = requests.get("https://oapi.dingtalk.com/gettoken?appkey=%s&appsecret=%s" % (self.app_key, self.app_secret)).json()["access_token"]

    def get_access_token(self):
        access_token = requests.get("https://oapi.dingtalk.com/gettoken?appkey=%s&appsecret=%s" % (self.app_key, self.app_secret))
        return access_token.json()["access_token"]

    def work_text_message_notify(self, notify_message, userid_list):
        message = {"agent_id": self.agent_id,
                   "msg": {"msgtype": "text",
                           "text":
                               {"content": notify_message}
                           },
                   "userid_list": userid_list
                   }
        api_res = self.request_session.post('https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2?access_token=%s' % (self.access_token),
                      headers={'Content-Type':'application/json'}, data=json.dumps(message), timeout=3)
        if api_res.json()["errcode"] == 0:
            return True
        else:
            print(api_res.text)
            return False

    def send_workorder_approval_message(self, workorder_obj, content, user_mail, approval_user_id):
        steps = AuditStep.objects.filter(workflow=workorder_obj.workflow).order_by('order_num')
        if workorder_obj.cur_step != steps.last():
            btn_json_list = [
                {
                    "title": "同意",
                    "action_url": "%s/api/v1/workflow/dingding_audit/?workorder_id=%s&user_id=%s&opinion=1" % (settings.PROJECT_URL, workorder_obj.id,approval_user_id)
                },
                {
                    "title": "驳回",
                    "action_url": "%s/api/v1/workflow/dingding_audit/?workorder_id=%s&user_id=%s&opinion=0" % (settings.PROJECT_URL,workorder_obj.id,approval_user_id)
                },
            ]
        else:
            if workorder_obj.cur_step == steps.last() and workorder_obj.workflow.script:
                btn_json_list = [
                    {
                        "title": "驳回",
                        "action_url": "%s/api/v1/workflow/dingding_audit/?workorder_id=%s&user_id=%s&opinion=0" % (settings.PROJECT_URL,workorder_obj.id,approval_user_id)
                    },
                    {
                        "title": "同意(自动执行)",
                        "action_url": "%s/api/v1/workflow/dingding_audit/?workorder_id=%s&user_id=%s&opinion=1" % (settings.PROJECT_URL,workorder_obj.id,approval_user_id)
                    },
                    {
                        "title": "同意(等待手工执行)",
                        "action_url": "%s/api/v1/workflow/dingding_audit/?workorder_id=%s&user_id=%s&opinion=2" % (settings.PROJECT_URL,workorder_obj.id,approval_user_id)
                    },
                ]
            else:
                btn_json_list = [
                    {
                        "title": "驳回",
                        "action_url": "%s/api/v1/workflow/dingding_audit/?workorder_id=%s&user_id=%s&opinion=0" % (
                        settings.PROJECT_URL, workorder_obj.id, approval_user_id)
                    },
                    {
                        "title": "同意",
                        "action_url": "%s/api/v1/workflow/dingding_audit/?workorder_id=%s&user_id=%s&opinion=1" % (
                        settings.PROJECT_URL, workorder_obj.id, approval_user_id)
                    },
                ]
        notify_message = "提交人: %s  \n\n  " \
                         "提交时间: %s  \n\n  " \
                         "工单类型: %s  \n\n  " \
                         "工单内容: \n\n%s" % (workorder_obj.creator.cname, workorder_obj.create_time, workorder_obj.cname, content)

        message = {"agent_id": self.agent_id,
                   "msg": {"msgtype": "action_card",
                           "action_card": {
                                "title": "OpenGalaxy工单审批",
                                "markdown": notify_message,
                                "btn_orientation": "1",
                                "btn_json_list": btn_json_list,
                           }
                   },
                   "userid_list": user_mail
        }
        api_res = self.request_session.post('https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2?access_token=%s' % (self.access_token),
                      headers={'Content-Type':'application/json'}, data=json.dumps(message), timeout=3)
        if api_res.json()["errcode"] == 0:
            return True
        else:
            print(api_res.text)
            return False
