#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-07 22:14
# author：WuShuang5

#添加成员页面
from selenium.webdriver.common.by import By
from test_appium.page.Base_Page import BasePage


class Addmanualpage(BasePage):

    #添加学员信息
    def addmember_manual(self):

        self.driver.find_element(By.XPATH, "//*[@resource-id='com.tencent.wework:id/b7m']").send_keys('不要了')
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.tencent.wework:id/fwi']").send_keys('13417480123')
        self.driver.find_element(By.XPATH, "//*[@text='保存后自动发送邀请通知']").click()
        self.driver.find_element(By.XPATH, "//*[@text='保存']").click()


    #验证是否添加成功
    def verify_ok(self):
        while True:
            ele2 = self.driver.find_elements(By.XPATH, "//*[@text='手动输入添加']")
            if len(ele2)>0:
                message = self.driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text
                assert message == '添加成功'
                break
            else:
                eleee = self.driver.find_elements(By.XPATH, "//*[@text='手机已存在于通讯录，无法添加']")
                if len(eleee) > 0:
                    self.driver.find_element(By.XPATH, "//*[@text='确定']").click()
                    self.driver.find_element(By.XPATH, "//*[@resource-id='com.tencent.wework:id/fwi']").send_keys(
                        '13011223333')
                    self.driver.find_element(By.XPATH, "//*[@text='保存']").click()











