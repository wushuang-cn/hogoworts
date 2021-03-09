#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-07 22:10
# author：WuShuang5
import logging
import time

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    dt =  time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    logging.basicConfig(filename='../logs/' + str(dt) + '.log', level=logging.INFO,force=True)

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def find(self,locator,timeout=20):
        '''获取存在元素'''
        logging.info(f'正在获取元素{locator}')
        try:
            return  WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        except Exception as e:
            self.driver.get_screenshot_as_file('/Screenshots/foo.png')
            logging.error(f"获取元素失败:{e}")

    def finds(self,locator,timeout=20):
        '''获取存在元素'''
        logging.info(f'正在获取元素{locator}')
        try:
            return  WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
        except Exception as e:
            self.driver.get_screenshot_as_file('/Screenshots/foo.png')
            logging.error(f"获取元素失败:{e}")

