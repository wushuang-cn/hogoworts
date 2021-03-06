#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
如何封装滑动查找？（swipe TouchAction）

完成企业添加联系人
"""
import time

from appium import  webdriver
from appium.webdriver.common import mobileby
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.pythoncode.moveaction import MoveAction


class TestAddmember():
    def setup(self):
        desired_caps = {'platformName': 'Android',
                        'plathformVersion': '10',
                        'deviceName': 'e5bddedb',
                        'appPackage': 'com.tencent.wework',
                        'appActivity': '.launch.LaunchSplashActivity',
                        'noReset': True,
                        'newCommandTimeout': 6000,
                        'automationName': 'UiAutomator2',
                        'dontStopAppOnReset': True, # 首次启动的时候 不停止app
                        'skipServerInstallation':True,
                        "skipServerInstallation": True,
                        "unicodeKeyBoard":True,
                        "resetKeyBoard":True
                        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)
    def teardown(self):
        self.driver.close()

    def test_add(self):

        #点击通讯录
        self.driver.find_element(By.XPATH,"//*[@resource-id='com.tencent.wework:id/en5' and @text='通讯录']").click()

        #如果没有找到’添加成员‘ 则往上滑动下

        while True:
            #点击添加学员
            add_ele = self.driver.find_elements(By.XPATH, "//*[@text='添加成员']")
            print(len(add_ele))
            MoveAction(self.driver, 4 / 5, 2 / 5).move_action()
            if len(add_ele)>0:
                add_ele[0].click()
                break
        #点击手动输入添加
        self.driver.find_element(By.XPATH,"//*[@text='手动输入添加']").click()

        self.driver.find_element(By.XPATH,"//*[@resource-id='com.tencent.wework:id/b7m']").send_keys('test001')
        self.driver.find_element(By.XPATH,"//*[@resource-id='com.tencent.wework:id/fwi']").send_keys('13417480117')
        self.driver.find_element(By.XPATH,"//*[@text='保存后自动发送邀请通知']").click()
        self.driver.find_element(By.XPATH,"//*[@text='保存']").click()


        def wait_ele(driver):
            ele2 = driver.find_elements(By.XPATH, "//*[@text='手动输入添加']")
            return  len(ele2) >0


        WebDriverWait(self.driver,30).until(wait_ele)
        print(self.driver.page_source)
        # message ="// *[contains( @ text,'成功')]"
        message=self.driver.find_element(By.XPATH,"//*[@class='android.widget.Toast']").text
        assert message=='添加成功'







