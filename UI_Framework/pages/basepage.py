#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-12 11:13
# author：WuShuang5

#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-07 22:10
# author：WuShuang5
import logging
import os
import time

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

'''
    把装饰器放在类外面
    在方法把self传进去，这样子就可以调用基类的方法（如finds、find等）
'''

def black_check(func):
    def wrapper( *args, **kwargs):
        self=args[0]
        try:
            return func(*args, **kwargs)
        except:
            print('正在获取黑名单')
            black_list = ['//*[@resource-id="miui:id/buttonPanel"]',
                          '//*[@resource-id="com.xueqiu.android:id/iv_close"]']
            for one in black_list:
                ele = self.finds(By.XPATH, one)
                if len(ele) > 0:
                    ele[0].click()
            return func(*args, **kwargs)
    return wrapper


class BasePage():

    dt = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    logging.basicConfig(filename='../logs/' + str(dt) + '.log', level=logging.INFO, force=True)

    def __init__(self,driver:WebDriver):
        self.driver=driver



    @black_check
    def find(self,locator,valuee):
        logging.info(f'正在获取元素{locator}/{valuee}')
        return self.driver.find_element(locator, valuee)


    def finds(self,locator,valuee):
        logging.info(f'正在获取元素{locator}/{valuee}')
        return  self.driver.find_elements(locator,valuee)


    def find_click(self,locator,valuee):
        logging.info(f'正在获取元素并点击{locator}/{valuee}')
        return self.find(locator,valuee).click()

    def find_sendkeys(self,locator,valuee,text):
        logging.info(f'正在获取元素并输入{locator}/{valuee}')
        return self.find(locator,valuee).send_keys(text)


    # def find(self,locator,timeout=20):
    #     dt = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    #     logging.basicConfig(filename='../logs/' + str(dt) + '.log', level=logging.INFO, force=True)
    #     '''获取存在元素'''
    #     logging.info(f'正在获取元素{locator}')
    #     try:
    #         return  WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
    #     except Exception as e:
    #         self.driver.get_screenshot_as_file('/Screenshots/foo.png')
    #         logging.error(f"获取元素失败:{e}")
    #
    # def finds(self,locator,timeout=20):
    #     '''获取存在元素'''
    #     logging.info(f'正在获取元素{locator}')
    #     try:
    #         return  WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
    #     except Exception as e:
    #         self.driver.get_screenshot_as_file('/Screenshots/foo.png')
    #         logging.error(f"获取元素失败:{e}")


    """函数前加上@classmethon，则该函数变为类方法，该函数只能访问到类的数据属性，不能获取实例的数据属性"""


    def get_screen_img(self):
        """"页面截图功能"""
        file_path = (os.path.abspath("..")) + '/screenshots/'
        now = time.strftime('%Y%m%d_%H%M%S')
        screen_name = file_path + now + '.png'

        try:

            self.driver.get_screenshot_as_file(screen_name)

        except NameError as na:
            logging.info("截图失败:%s")
            self.get_screen_img()






