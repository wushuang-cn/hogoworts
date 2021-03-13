#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-12 11:11
# author：WuShuang5

import logging
import time

from selenium.webdriver.common.by import By

from UI_Framework.pages.basepage import BasePage
from UI_Framework.pages.market import  MarketPage

dt = time.strftime('%Y%m%d_%H%M%S')
logging.basicConfig(filename='run_' + str(dt) + '.log', level=logging.INFO)





class MainPage(BasePage):
    def goto_marketpage(self):

        logging.info('点击行情')
        self.find_click(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/post_status"]')
        self.find_click(By.XPATH,'//*[@text="行情"]')
        return MarketPage(self.driver)