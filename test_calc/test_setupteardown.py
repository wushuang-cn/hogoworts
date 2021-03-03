# -*- coding:utf-8 -*-

def setup_module():
    print('模块级setup_module【最高】')
def teardown_module():
    print('模块级teardown_module【最高】')

def setup_function(self):
        print('函数级：setup_function，每个def函数前后都执行一次（放在类中不生效）')
def teardown_function(self):
    print('函数级：teardown_function，每个def函数前后都执行一次（放在类中不生效）')

def test_case1():
    print('test_case1')

def test_case2():
    print('test_case2')

class TestDemo1:
    def setup_class(self):
        print('TestDemo1类级setup_class:只执行一次【高】')
    def teardown_class(self):
        print('TestDemo1类级teardown_class:只执行一次【高】')
    # def setup_function(self): 放在类中不生效
    #     print('函数级：setup_function')
    # def teardown_function(self):
    #     print('函数级：teardown_function')
    def setup_method(self):
        print('方法级：setup_method，就相当于setup_method')
    def teardown_method(self):
        print('方法级：teardown_method,，就相当于teardown_method')
    def setup(self):
        print('setup')
    def teardown(self):
        print('teardown')
    def test_case3(self):
        print('test_case3')

    def test_case4(self):
        print('test_case4')


class TestDemo2:
    def setup_class(self):
        print('TestDemo2类级setup_class:只执行一次')

    def teardown_class(self):
        print('TestDemo2类级teardown_class:只执行一次')

    # def setup_function(self): 放在类中不生效
    #     print('函数级：setup_function')
    #
    # def teardown_function(self):
    #     print('函数级：teardown_function')

    def setup_method(self):
        print('方法级：setup_method,每个方法始末都会执行一次')

    def teardown_method(self):
        print('方法级：teardown_method,每个方法始末都会执行一次')

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def test_case5(self):
        print('test_case5')

    def test_case6(self):
        print('test_case6')