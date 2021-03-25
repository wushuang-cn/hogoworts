#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-25 21:09
# author：WuShuang5
import pytest
import requests
from test_request.page.basepage import BasePage

'''作业：实现通讯录增删改查+代理'''
class TestQiye(BasePage):
    def setup(self):
        self.url = self.get_ymldata('env', 'test')
        self.url_user = self.get_ymldata('env', 'test_user')
        self.corpid = self.get_ymldata('corpid')
        self.corpsecret = self.get_ymldata('corpsecret')
        self.token = self.get_token()

    def get_token(self):

        url=f'https://{self.url}/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}'
        r=requests.get(url=url)
        print(r)
        return  r.json()['access_token']

    @pytest.mark.run(order=0)
    def test_query(self):
        userid='WuShuang'
        url=f'https://{self.url_user}/get?access_token={self.token}&userid={userid}'
        # proxies = {
        #     "https": "http://127.0.0.1:9999",
        #     "http": "http://127.0.0.1:9999"
        # }
        #r=requests.get(url=url,proxies=proxies,verify=False)
        r=requests.get(url)
        self.assert_code(r)
        assert r.json()["name"]=='吴双'

    @pytest.mark.run(order=1)
    def test_creat(self):
        url=f'https://{self.url_user}/create?access_token={self.token}'
        payload={

                "userid": "zhangsan",
                "name": "张三",
                "mobile": "+86 13800000000",
                "department": [2]
        }
        r=requests.post(url=url,json=payload)
        self.assert_code(r)

    @pytest.mark.run(order=2)
    def test_update(self):
        url=f'https://{self.url_user}/update?access_token={self.token}'
        payload={
            "userid": "zhangsan",
            "name": "小王把"
        }
        r = requests.post(url=url, json=payload)
        self.assert_code(r)

    @pytest.mark.run(order=3)
    def test_delete(self):
        userid='zhangsan'
        url=f'https://{self.url_user}/delete?access_token={self.token}&userid={userid}'
        r = requests.get(url)
        self.assert_code(r)


