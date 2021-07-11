#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-07-11 16:35
# author：WuShuang5
import yaml

import requests

from test_feishu.common import gettoken

with open('../data/cal.yml',encoding='utf-8') as f:
    datayml_create = yaml.safe_load(f)['create']


def cal_create():
    url = 'https://open.feishu.cn/open-apis/calendar/v4/calendars'
    abc = "Bearer " + gettoken()

    headers = {
        "Authorization": abc,
        "Content-Type": "application/json; charset=utf-8"
    }
    data = {
        "summary": datayml_create["summary"],
        "description": datayml_create["description"],
        "permissions": "private",
        "color": -1,
        "summary_alias": datayml_create["summary_alias"]
    }

    res = requests.post(url=url, headers=headers, json=data)
    return res.json()