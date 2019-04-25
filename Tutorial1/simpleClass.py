#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:03:38 2019

@author: sharon
"""

class SimpleClass:
    
    # static variable
    stat = 10
    def __init__(self,a,b):
        # parametrized constructor/ also a dunder method
        self.a = a
        self.b = b
    
    def __repr__(self):
        # dunder method
        return "<a: {}, b: {}, stat: {} type: {}>".format(self.a, self.b, self.stat,type(self))
    
    def fun1(self,num):
        '''
        Instance method can access anything in the class.
        Need to do object creation to call this function.
        '''
        self.a = self.b + num
        # accessing static variable
        self.b = self.stat + num
        
    
    @staticmethod
    def fun2(num):
        '''
        Static method cannot access anything in the class.
        It's totally a self contained code.
        No need of object creation to call this function.
        '''
        return num**2
    
    @classmethod
    def fun3(cls,num):
        '''
        Class method can access anything in the class.
        No need of object creation to call this function.
        It has the power to change the static variables. Without creating objects.
        '''
        cls.stat = cls.fun2(num)
        
        
if __name__ == "__main__":

    # classmethod example
    obj1 = SimpleClass(2,30)
    print("Before calling fun3: ",obj1)
    
    SimpleClass.fun3(3)
    print("After calling fun3: ",obj1)
    
    # static method example
    print("Calling static method: ",SimpleClass.fun2(8))
    
    # instance method example
    print("Before calling instance method:",obj1)
    obj1.fun1(8)
    print("After calling instance method:",obj1)
    