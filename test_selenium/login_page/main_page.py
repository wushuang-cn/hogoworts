from selenium import webdriver

from test_selenium.login_page.contacts_page import Contactspage


class Mainpage:
    def __init__(self):
        # ���� chrome �Ĳ���
        chrome_arg = webdriver.ChromeOptions()
        # ������Ե�ַ
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.implicitly_wait(3)

    #����ͨѶ¼
    def goto_contacts(self):
        self.driver.find_element_by_id('menu_contacts').click()
        return Contactspage(self.driver)
