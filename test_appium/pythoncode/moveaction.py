#! /usr/bin/env python
# -*- coding:utf-8 -*-
from appium.webdriver.common.touch_action import TouchAction

"""
如何封装滑动查找？（swipe TouchAction）

完成企业添加联系人
"""

class MoveAction():
    def __init__(self,driver,y_start,y_end):
        self.driver=driver
        self.y_start=y_start
        self.y_end=y_end
    def move_action(self):
        action=TouchAction(self.driver)
        window_rect=self.driver.get_window_rect()
        #返回结果{"width":1080,"height":2131,"x":0,"y":0}
        width=window_rect['width']

        height=window_rect['height']
        x1=float(width/2)
        start=float(height*(self.y_start))
        end=float(height*(self.y_end))
        action.press(x=x1,y=start).wait(200).move_to(x=x1,y=end).release().perform()
