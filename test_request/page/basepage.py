#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-25 22:32
# author：WuShuang5
import yaml


class BasePage:


    def assert_code(self,r):
        assert r.json()["errcode"] == 0
    def get_ymldata(self,key,datatype=None):
        with open('../data/data.yml','r',encoding='utf-8') as f:
            data=yaml.safe_load(f)
            if datatype:
                return data[key][datatype]
            else:
                return data[key]


if __name__=='__main__':
    a=BasePage()
    print(a.get_ymldata('env','test'))
    print(a.get_ymldata('corpid'))