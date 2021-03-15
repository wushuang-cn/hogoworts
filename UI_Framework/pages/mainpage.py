#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-12 11:11
# author：WuShuang5


from UI_Framework.pages.basepage import BasePage
from UI_Framework.pages.market import  MarketPage



class MainPage(BasePage):
    def goto_marketpage(self):

        self.base_operator('../datas/mainpage.yml','MainPage')
        return MarketPage(self.driver)