# -*- coding:utf-8 -*-
import pytest


@pytest.fixture(params=['Tom','Lily','Winnie'])
def login(request):
    print('登录')
    return  request.param

def test_order(login):
    print(login) #注意此处函数不加括号，不用执行login该函数
    print('下单')
