#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-12 11:13
# author：WuShuang5

#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-07 22:10
# author：WuShuang5

import os
import time
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from UI_Framework.pages.log import loginit, logger


def black_check(func):
    def wrapper( *args, **kwargs):
        self=args[0]
        try:
            return func(*args, **kwargs)
        except:
            logger.info('正在遍历黑名单')
            black_list = ['//*[@resource-id="miui:id/buttonPanel"]',
                          '//*[@resource-id="com.xueqiu.android:id/iv_close"]']
            for one in black_list:
                ele = self.finds(By.XPATH, one)
                if len(ele) > 0:
                    ele[0].click()
            return func(*args, **kwargs)
    return wrapper


class BasePage():

    # dt = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    # logging.basicConfig(filename='../logs/' + str(dt) + '.log', level=logging.INFO, force=True)

    def __init__(self,driver:WebDriver):
        self.driver=driver



    @black_check
    def find(self,locator,valuee):
        logger.info(f'正在查找元素{valuee}')

        return self.driver.find_element(locator, valuee)


    def finds(self,locator,valuee):
        logger.info(f'正在查找多个元素{valuee}')

        return  self.driver.find_elements(locator,valuee)


    def find_click(self,locator,valuee):
        logger.info(f'正在查找并点击元素{valuee}')

        return self.find(locator,valuee).click()

    def find_sendkeys(self,locator,valuee,text):
        logger.info(f'正在查找元素赋值{valuee}/{text}')

        return self.find(locator,valuee).send_keys(text)

    """函数前加上@classmethon，则该函数变为类方法，该函数只能访问到类的数据属性，不能获取实例的数据属性"""

    def get_screen_img(self):
        """"页面截图功能"""
        file_path = (os.path.abspath("..")) + '/screenshots/'
        now = time.strftime('%Y%m%d_%H%M%S')
        screen_name = file_path + now + '.png'

        try:
            logger.info(f'正在截图{screen_name}')
            self.driver.get_screenshot_as_file(screen_name)

        except NameError as na:
            logger.error('截图失败')
            self.get_screen_img()

    """
        解析从yaml文件中取得数据
    """
    def base_operator(self,filename,pagename):
        with open(filename, 'r',encoding='gbk') as f:
            data = yaml.safe_load(f)
            logger.info(f'从文件{filename}获取数据{pagename}')
            for step in data[pagename]:
                if step['action'] == 'find_click':
                    self.find_click(step['locator'], step['value'])
                elif step['action'] == 'find_sendkeys':
                    self.find_sendkeys(step['locator'], step['value'], step['text'])
                elif step['action'] == 'find':
                    return self.find(step['locator'], step['value']).text







