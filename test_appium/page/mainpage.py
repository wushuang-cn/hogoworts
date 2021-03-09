#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-08 16:19
# author：WuShuang5
import logging
import time

from selenium.webdriver.common.by import By

from test_appium.page.Base_Page import BasePage
from test_appium.page.contacts_page import Contacts_page

dt = time.time()
logging.basicConfig(filename='run_' + str(dt) + '.log', level=logging.INFO)
class MainPage(BasePage):
    def goto_contactspage(self):
        # 点击通讯录
        logging.info('点击通讯录')
        ele_txl=(By.XPATH,"//*[@resource-id='com.tencent.wework:id/en5' and @text='通讯录']")
        self.find(ele_txl).click()
        #self.driver.find_element(By.XPATH, "//*[@resource-id='com.tencent.wework:id/en5' and @text='通讯录']").click()
        return Contacts_page(self.driver)