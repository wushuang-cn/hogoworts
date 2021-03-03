# -*- coding:utf-8 -*-

'''
编写计算器加减乘除
'''
import yaml

import pytest

from Hogwots.pythoncode.Calculator import Calculator
from Hogwots.pythoncode.getYamldatas import get_yamldatas


class TestCal():


    def setup_class(self):
        print('开始计算')
        self.cal = Calculator()
    def teardown_class(self):
        print('计算结束')



    @pytest.mark.cal1
    #@pytest.mark.parametrize(('a','b','result'),[(1,1,2),(2,2,4),(100,100,300)])
    #@pytest.mark.parametrize(('a','b','result'),yaml.safe_load(open("../Datas/data1.yml")))
    # @pytest.mark.parametrize(('a','b','result'),get_yamldatas('add'),ids=get_yamldatas('add','ids'))
    #此处参数化 会被当做3个测试用例 分别执行，执行结果不影响其他用例
    # def test_add(self,a,b,result):
    #     assert  self.cal.add(a,b)==result
    #     print(f'a={a},b={b},result={result}')
    def test_add_positive(self,get_add_postive):
        assert self.cal.add(get_add_postive[0], get_add_postive[1]) == get_add_postive[2]

    def test_add_illegal_1(self,get_add_illegal_1):
        f=get_add_illegal_1
        print(f'a={f[0]},b={f[1]},result={f[2]}')
        assert    self.cal.add(f[0],f[1])==f[2]

    def test_add_illegal_2(self,get_add_illegal_2):
        f=get_add_illegal_2
        print(f'a={f[0]},b={f[1]},result={f[2]}')
        assert  round(self.cal.add(f[0],f[1]),1)==f[2]

    #@pytest.mark.cal11
    #此处使用for循环来执行用例，只会当作1个用例执行，其中一个错误就被认为该用例错误
    # def test_add1(self):
    #     datas=[(1,1,2),(2,2,4),(100,100,300)]
    #     for data in datas:
    #         assert  self.cal.add(data[0],data[1])==data[2]

    '''
    除法：注意被除数不能为0，不能为非数字
    '''

    #@pytest.mark.parametrize(('a', 'b', 'result'), get_yamldatas('div'),ids=get_yamldatas('div','ids'))
    # def test_div(self,a,b,result):
    #     assert self.cal.div(a,b)==result
    #     print(f'a={a},b={b},result={result}')



