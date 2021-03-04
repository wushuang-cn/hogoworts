#! /usr/bin/env python
# -*- coding:utf-8 -*-


import pytest
from selenium.webdriver.support.wait import WebDriverWait

'''
添加成员详细操作
'''
#第二次作业11
class Addmember():
    def __init__(self,driver):
        self.driver=driver

    def add_member(self):

        self.driver.find_element_by_id('username').send_keys('wutest')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('wutest')
        self.driver.find_element_by_id('memberAdd_phone').send_keys('13612845422')
        self.driver.find_elements_by_class_name('qui_btn.ww_btn.js_btn_save')[1].click()