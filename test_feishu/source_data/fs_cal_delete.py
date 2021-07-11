#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-07-11 16:35
# author：WuShuang5
import requests

from test_feishu.common import mytoken
from test_feishu.source_data.fs_cal_create import cal_create

calendar_id=cal_create()["data"]["calendar"]['calendar_id']

def cal_delete():
    url = 'https://open.feishu.cn/open-apis/calendar/v4/calendars/'+calendar_id


    headers = {
        "Authorization": mytoken,
        "Content-Type": "application/json; charset=utf-8"
    }



    res = requests.delete(url=url, headers=headers)

    return  res.json()
