#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-07-11 15:01
# author：WuShuang5
import yaml

import requests


with open('../data/cal.yml',encoding='utf-8') as f:
    datayml_create = yaml.safe_load(f)

def gettoken():
    url='https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'
    headers={
        "Content-Type":"application/json; charset=utf-8"
    }
    data={
        "app_id":"cli_a060291ac578900c",
        "app_secret":"2WOa6JF6REGYnvwXBnmcpfRG1oSoNn6J"
    }
    res=requests.post(url=url,json=data,headers=headers)
    # {'code': 0, 'expire': 7163, 'msg': 'ok', 'tenant_access_token': 't-ab78bf80fa668987aca7f21c1c6d601ea64175a3'}
    return res.json()["tenant_access_token"]

mytoken = "Bearer " + gettoken()

if __name__=="__main__":
    t=gettoken()
    print(t)