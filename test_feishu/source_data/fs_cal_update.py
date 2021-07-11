#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-07-11 16:35
# author：WuShuang5
import yaml

import requests

from test_feishu.common import gettoken
from test_feishu.source_data.fs_cal_create import cal_create

calendar_id=cal_create()["data"]["calendar"]['calendar_id']
with open('../data/cal.yml',encoding='utf-8') as f:
    datayml_upd = yaml.safe_load(f)['update']

def cal_update():
    url = 'https://open.feishu.cn/open-apis/calendar/v4/calendars/'+calendar_id
    abc = "Bearer " + gettoken()

    headers = {
        "Authorization": abc,
        "Content-Type": "application/json; charset=utf-8"
    }
    data = {
        "summary": datayml_upd["summary"],
        "description": datayml_upd["description"],
        "permissions": "private",
        "color": -1,
        "summary_alias": datayml_upd["summary_alias"]
    }

    res = requests.patch(url=url, headers=headers, json=data)
    return res.json()