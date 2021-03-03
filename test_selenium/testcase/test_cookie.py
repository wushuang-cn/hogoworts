#! /usr/bin/env python
# -*- coding:utf-8 -*-
import json
import time

from selenium import webdriver

'''
1.使用浏览器利用及 selenium cookie 方法，进行企业微信登陆，将代码（或 github 链接）贴到帖子下面1
'''
class TestDemo():

    def setup_class(self):
        # 声明 chrome 的参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome() #options=chrome_arg
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.implicitly_wait(3)

    def test_addcookie(self):
        '''
        获取cookies并存入文件
        cookies = self.driver.get_cookies()
        print(cookies)
        with open('../tmp.txt', 'w', encoding='utf-8') as f:
            f.write(json.dumps(cookies))

        '''



        with open('../tmp.txt', 'r', encoding='utf-8') as f:
            '''
            使用json.loads
            #raw_cookies=f.read() #是个str类型
            for one in json.loads(raw_cookies):
            '''
            #使用json.load

            raw_cookies = json.load(f)
            for one in raw_cookies:
                self.driver.add_cookie(one)
            self.driver.refresh()
            time.sleep(3)

