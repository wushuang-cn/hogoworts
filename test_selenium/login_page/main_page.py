from selenium import webdriver

from test_selenium.login_page.contacts_page import Contactspage


class Mainpage:
    def __init__(self):
        # 声明 chrome 的参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.implicitly_wait(3)

    #进入通讯录
    def goto_contacts(self):
        self.driver.find_element_by_id('menu_contacts').click()
        return Contactspage(self.driver)
