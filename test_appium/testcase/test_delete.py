#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-07 22:34
# author：WuShuang5

from test_appium.page.app import App


class TestDelete():
    def setup_class(self):
        self.step = App()
        self.step.start_app()

    def teardown_class(self):
        self.step.stop_app()


    def test_delete(self):
        delete_member = self.step.goto_main().goto_contactspage().click_person().goto_personeditpage().goto_personedit()
        delete_member.person_edit()
        delete_member.verfy_okk()
