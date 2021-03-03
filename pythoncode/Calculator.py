# -*- coding:utf-8 -*-

'''
编写计算器加减乘除
'''
class Calculator:
    def add(self,a,b):
        try:
            if isinstance(a,int) and  isinstance(b,int):
                return a+b
            elif isinstance(a,float) and  isinstance(b,float):
                return a+b
            elif isinstance(a,int) and  isinstance(b,float):
                return a+b
            elif isinstance(a,float) and  isinstance(b,int):
                return a+b
        except Exception as e:
            return False
            print(f'此处错误信息：{e}')


    def minus(self,a,b):
        return a-b
    def multi(self,a,b):
        return a*b
    def div(self,a,b):
        try:
            return a / b
        except Exception as e:
                print(f'此处有异常：{e}')

if __name__=='__main__':
    c=Calculator()
    print(c.add('o', 9.9))