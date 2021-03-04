#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
通讯录页面 点击添加成员
'''
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test_selenium.login_page.addmember_page import  Addmember

#第二次作业
class Contactspage:

    def __init__(self,driver):
        self.driver=driver

    def goto_add(self):

        def wait_name(driver):
            WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.qui_btn.ww_btn.js_add_member')))
            driver.find_elements_by_css_selector('.qui_btn.ww_btn.js_add_member')[2].click()
            eles = driver.find_elements_by_id('username')
            if len(eles) > 0:
                return True
            else:
                return False

        WebDriverWait(self.driver, 30).until(wait_name)
        return Addmember(self.driver)