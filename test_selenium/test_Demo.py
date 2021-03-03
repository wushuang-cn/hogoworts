#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
作业：
1.使用浏览器利用及 selenium cookie 方法，进行企业微信登陆，将代码（或 github 链接）贴到帖子下面
2.利用 PO 封装添加成员
'''
import json
import time

import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo():

    def setup_class(self):
        # 声明 chrome 的参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def test_tongxunlu(self):
        self.driver.find_element_by_id('menu_contacts').click()

    @pytest.fixture()
    def wait_name(self):

        self.driver.find_elements_by_css_selector('.qui_btn.ww_btn.js_add_member')[1].click()
        eles=self.driver.find_element_by_id('username')
        return  eles>0

    def test_add(self,wait_name):

        WebDriverWait(self.driver, 60).until(wait_name)


        self.driver.find_element_by_id('username').send_keys('吴11')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('吴11')
        self.driver.find_element_by_id('memberAdd_phone').send_keys('13612845421')
        self.driver.find_element_by_id('.qui_btn.ww_btn.js_btn_save').click()

    def test_addcookie(self):
        '''
        获取cookies并存入文件
        :return:
        '''
        # cookies=self.driver.get_cookies()
        # print(cookies)
        # with open('tmp.txt','w',encoding='utf-8') as f:
        #     f.write(json.dumps(cookies))   #将python对象转化为文本可存储
        '''
        读取文件中的cookies
        '''
        with open('tmp.txt','r',encoding='utf-8') as f:

            '''
            使用json.loads
            #raw_cookies=f.read() #是个str类型
            for one in json.loads(raw_cookies):
            '''
            '''
            使用json.load
            '''
            raw_cookies = json.load(f)
            for one in raw_cookies:
                print(one)
                self.driver.add_cookie(one)
            self.driver.refresh()
            time.sleep(3)




