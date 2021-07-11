#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-07-11 16:35
# author：WuShuang5
import yaml

import requests

from test_feishu.common import mytoken
from test_feishu.source_data.fs_cal_create import cal_create
from test_feishu.common import datayml_create

calendar_id=cal_create()["data"]["calendar"]['calendar_id']


def cal_update():
    url = 'https://open.feishu.cn/open-apis/calendar/v4/calendars/'+calendar_id


    headers = {
        "Authorization": mytoken,
        "Content-Type": "application/json; charset=utf-8"
    }
    data = {
        "summary": datayml_create["update"]["summary"],
        "description": datayml_create["update"]["description"],
        "permissions": "private",
        "color": -1,
        "summary_alias": datayml_create["update"]["summary_alias"]
    }

    res = requests.patch(url=url, headers=headers, json=data)
    return res.json()