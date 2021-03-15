#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-12 11:14
# author：WuShuang5

from UI_Framework.pages.basepage import BasePage


class MarketPage(BasePage):
    """搜索贵州茅台股价"""
    def search_price(self):
        steps=self.base_operator("../datas/marketpage.yml",'MarketPage')




