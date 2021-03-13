#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-12 11:14
# author：WuShuang5
from selenium.webdriver.common.by import By

from UI_Framework.pages.basepage import BasePage


class MarketPage(BasePage):
    """搜索贵州茅台股价"""
    def search_price(self):
        self.find_click(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/action_search"]')
        self.find_sendkeys(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/search_input_text"]','贵州茅台')

        # ele=self.finds(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/listview"]/android.widget.RelativeLayout[1]"]')
        # print(len(ele))
        self.find_click(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/name"]')



        return  self.find(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/current_price"]').text




