#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-12 11:11
# author：WuShuang5

'''
作业：
    提取基础框架，用框架实现雪球的点击行情，并查找贵州茅台股价

    将黑名单功能放到装饰器，装饰 find 方法 （提高）

'''
from UI_Framework.pages.app import App


class TestMarket():
    def setup(self):
        self.t=App()
        self.t.start_app()
    def test_serchmaket(self):
        price_mt=self.t.goto_main().goto_marketpage().search_price()

        assert float(price_mt)>2000