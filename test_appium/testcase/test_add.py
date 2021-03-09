#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-07 22:34
# author：WuShuang5

from test_appium.page.app import App


class TestAdd():
    def setup_class(self):
        self.step=App()
        self.step.start_app()



    def teardown_class(self):
        self.step.stop_app()


    def test_add(self):
        add_member=self.step.goto_main().goto_contactspage().goto_add().add_manual()
        add_member.addmember_manual()
        add_member.verify_ok()
