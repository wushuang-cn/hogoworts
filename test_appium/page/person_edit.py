#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-07 22:13
# author：WuShuang5


#编辑成员页面
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.Base_Page import BasePage


class PersonEdit(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver

    def person_edit(self):
        # 点击删除成员按钮
        ele_del=(By.XPATH, "//*[@text='删除成员']")
        self.find(ele_del).click()

        # 点击弹出框的确定按钮
        ele_sure=(By.XPATH, "//*[@text='确定']")
        self.find(ele_sure).click()

    def verfy_okk(self):
        # 验证是否删除成功

        locator=(By.XPATH,"//*[@text='我的客户']")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(locator))

        self.driver.find_element(By.XPATH, "//*[@text='不要了1']")

