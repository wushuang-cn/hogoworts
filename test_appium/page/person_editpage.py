#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-07 22:13
# author：WuShuang5


#个人信息页面2
from selenium.webdriver.common.by import By

from test_appium.page.Base_Page import BasePage
from test_appium.page.person_edit import PersonEdit


class Personeditpage(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver

    def goto_personedit(self):
        # 点击编辑成员按钮

        ele_edit=(By.XPATH, "//*[@text='编辑成员']")
        self.find(ele_edit).click()
        return PersonEdit(self.driver)