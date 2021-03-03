# -*- coding:utf-8 -*-
import pytest


class TestFixture():
    # @pytest.fixture(autouse=True) 加上autouse参数后 会在每个函数前都自动执行

    @pytest.fixture()
    def login(self):
        print('登录')
        yield  # yield后面的步骤都会在调用login函数并且完成自身函数执行后 操作！！！！
        print('恭喜都完成啦')

    # @pytest.fixture()
    # def hello(self,login):
    #     print('欢迎')

    #方式一：  在方法里写入函数名调用
    def test_order(self,login):
        print('下单')

    #方式二： 使用
    #@pytest.mark.usefixtures("login")

    def test_register(self):
        print('请注册')

    def test_search(self,login):
        print('浏览商品')