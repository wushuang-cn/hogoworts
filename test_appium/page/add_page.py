#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-07 22:13
# author：WuShuang5


#添加成员页面
from selenium.webdriver.common.by import By

from test_appium.page.Base_Page import BasePage
from test_appium.page.addmanual_page import Addmanualpage


class Addpage(BasePage):

    # def __init__(self,driver):
    #     self.driver=driver

    #点击手动输入添加
    def add_manual(self):
        self.driver.find_element(By.XPATH, "//*[@text='手动输入添加']").click()
        return Addmanualpage(self.driver)
