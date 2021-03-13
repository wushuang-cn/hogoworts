#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-12 11:14
# author：WuShuang5

#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-07 22:11
# author：WuShuang5


import time
import yaml

from appium import  webdriver
from appium.webdriver.common import mobileby
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



#初始化 进入app首页
from UI_Framework.pages.mainpage import MainPage

with open('../datas/data.yml') as f:
     desired_caps=yaml.safe_load(f)['desired_caps']

class App:

    '''初始化driver或者复用driver'''
    def start_app(self,driver=None):
        if driver==None:
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(20)
        else:
            self.driver.launch_app()



    def stop_app(self):
        #停止app
        self.driver.quit()

    def restart(self):
        # 重启app
        self.driver.close_app()

        #如果被测应用已关闭或在后台运行，它将启动它。如果AUT已打开，它将使其放到后台并重新启动
        self.driver.launch_app()


    #进入主页
    def goto_main(self):
        return MainPage(self.driver)

