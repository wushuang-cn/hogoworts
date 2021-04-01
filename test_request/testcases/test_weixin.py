#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-30 20:48
# author：WuShuang5

'''封装好 base 类，实现 session 控制（把 token 加入到 session 中），加入测试用例（包含通讯录的增删改查）'''
from test_request.page.qiyeweixin import Qiyeweixin


class TestWeixin:

    def setup_class(self):
        self.qywx=Qiyeweixin()
        self.userid = 'zhangsan'
        self.name = '张三'
        self.mobile = '13612845422'
        self.department = [1]

    def teardown_class(self):
        pass
    def setup(self):
        pass
    def teardown(self):
        self.qywx.weixin_delete(self.userid)


    def test_creat(self):
        self.test_delete()
        r=self.qywx.weixin_creat(self.userid,self.name,self.mobile,self.department)

        assert r.get('errmsg')=='created'
        #断言
        info=self.qywx.weixin_query(self.userid)

        assert info.get('name')==self.name




    def test_query(self):
        r=self.qywx.weixin_creat(self.userid,self.name,self.mobile,self.department)
        assert r.get('errmsg') == 'created'
        info=self.qywx.weixin_query(self.userid)
        print('info')
        assert info.get('name')==self.name



    def test_update(self):
        self.qywx.weixin_creat(self.userid,self.name,self.mobile,self.department)
        newname=self.name+'ws'
        r=self.qywx.weixin_update(self.userid,newname)
        assert r.get('errmsg')=='updated'
        info=self.qywx.weixin_query(self.userid)
        assert info.get('name')==newname


    def test_delete(self):
        r=self.qywx.weixin_creat(self.userid,self.name,self.mobile,self.department)

        assert r.get('errmsg') == 'created'

        info=self.qywx.weixin_delete(self.userid)

        assert info.get('errmsg') == 'deleted'