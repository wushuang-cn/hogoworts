#! /usr/bin/env python
# -*- coding:utf-8 -*-
from test_selenium.login_page.main_page import Mainpage


class TestAddmember():
    def test_add(self):
        a=Mainpage()
        a.goto_contacts().goto_add().add_member()