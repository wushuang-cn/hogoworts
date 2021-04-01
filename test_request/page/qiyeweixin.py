#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-30 20:53
# author：WuShuang5
import pytest
import requests
import yaml

from test_request.page.basepage import BasePage


class Qiyeweixin(BasePage):



    def weixin_query(self,userid):

        url = f'https://{self.url_user}/get?userid={userid}'
        # proxies = {
        #     "https": "http://127.0.0.1:9999",
        #     "http": "http://127.0.0.1:9999"
        # }
        # r=requests.get(url=url,proxies=proxies,verify=False)
        r=self.send('get',url=url)
        return r.json()



    def weixin_creat(self,userid,name,mobile,department):
        url = f'https://{self.url_user}/create'
        payload = {

            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r=self.send('post',url=url, json=payload)
        return r.json()




    def weixin_update(self,userid,newname):

        url = f'https://{self.url_user}/update'
        payload = {
            "userid": userid,
            "name": newname
        }
        r= self.send('post',url=url, json=payload)
        return r.json()




    def weixin_delete(self,userid):

        url = f'https://{self.url_user}/delete?userid={userid}'
        r= self.res.request('get',url=url)
        return r.json()


if __name__=='__main__':
    t=Qiyeweixin()
    t.weixin_creat()
    t.weixin_query()
    t.weixin_update()
    t.weixin_delete()