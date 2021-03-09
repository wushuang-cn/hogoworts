#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-07 22:11
# author：WuShuang5
from selenium.webdriver.common.by import By

from test_appium.page.Base_Page import BasePage
from test_appium.page.add_page import Addpage
from test_appium.page.person_page import Personpage
from test_appium.pythoncode.moveaction import MoveAction



#通讯录页面




class Contacts_page(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver

    #点击添加成员
    def goto_add(self):
        while True:
            #点击添加学员
            ele_add=(By.XPATH, "//*[@text='添加成员']")
            add_ele=self.finds(ele_add)
            if add_ele:
                add_ele[0].click()
                break
            else:
                MoveAction(self.driver, 4 / 5, 2 / 5).move_action()
        return Addpage(self.driver)

    #点击某学员并删除
    def click_person(self):
        # 进入个人页面

        ele_name=(By.XPATH, "//*[@text='不要了1']")
        self.finds(ele_name).click()
        return Personpage(self.driver)
        # eles=self.driver.find_elements(By.XPATH, "//*[@text='不要了']")
        # print(eles)
        # if len(eles)>0:
        #     for i in range(len(eles)):
        #         print(f'第{i}次循环')
        #         eles[i].click()
        #         return Personpage(self.driver)
        # else:
        #     raise ( "找不到该元素")