#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-25 22:32
# author：WuShuang5
import requests
import yaml


class BasePage:
    def __init__(self):
        self.res = requests.Session()
        self.url = self.get_ymldata('env', 'test')
        self.url_user = self.get_ymldata('env', 'test_user')
        self.corpid = self.get_ymldata('corpid')
        self.corpsecret = self.get_ymldata('corpsecret')

        self.token = self.get_token()
        self.res.params = {'access_token': self.token}

    def get_token(self):
        url = f'https://{self.url}/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}'
        r = self.send(method='get', url=url)

        return r.json()['access_token']

    def assert_code(self,r):
        assert r.json()["errcode"] == 0
    def get_ymldata(self,key,datatype=None):
        with open('../data/data.yml','r',encoding='utf-8') as f:
            data=yaml.safe_load(f)
            if datatype:
                return data[key][datatype]
            else:
                return data[key]

    def send(self,*args,**kwargs):
        return self.res.request(*args,**kwargs)

if __name__=='__main__':
    a=BasePage()
    print(a.get_ymldata('env','test'))
    print(a.get_ymldata('corpid'))