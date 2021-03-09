#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-07 22:12
# author：WuShuang5


#个人信息页面
from selenium.webdriver.common.by import By

from test_appium.page.Base_Page import BasePage
from test_appium.page.person_editpage import Personeditpage


class Personpage(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver

    def goto_personeditpage(self):

        ele_tb=(By.XPATH,"//*[@text='个人信息']/../../../../following-sibling::android.widget.LinearLayout//android.widget.TextView")
        self.find(ele_tb).click()
        return Personeditpage(self.driver)