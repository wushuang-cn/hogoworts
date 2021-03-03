# -*- coding:utf-8 -*-
import pytest


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)

import yaml


def get_yamldatas_fixture(key,type='positive'):
    #datas=yaml.safe_load(open("../Datas/data1.yml"))
    with open("../Datas/data1.yml") as f:
        data=yaml.safe_load(f)

    return data[key][type]['datas'],data[key][type]['ids']

@pytest.fixture(params=get_yamldatas_fixture('add')[0],ids=get_yamldatas_fixture('add')[1])
def get_add_postive(request):
    return request.param

@pytest.fixture(params=get_yamldatas_fixture('add',type='illegal-1')[0],ids=get_yamldatas_fixture('add',type='illegal-1')[1])
def get_add_illegal_1(request):
    return request.param

@pytest.fixture(params=get_yamldatas_fixture('add',type='illegal-2')[0],ids=get_yamldatas_fixture('add',type='illegal-2')[1])
def get_add_illegal_2(request):
    return request.param


if __name__=='__main__':
    print(get_yamldatas_fixture('add')[0]) #为数据
    print(get_yamldatas_fixture('add')[1])#为ids