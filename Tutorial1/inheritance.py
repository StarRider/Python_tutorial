#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:03:27 2019

@author: sharon
"""
'''
Inheritance is the way by which a class can aquire the properties of another
class. It allows code reusablity. Better modelling of real life problems and
scenarios. 
The type of inheritance used here is multi-level inheritance.

Human---->Father---->Son
'''



class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class Father(Human):    
    def __init__(self,name,age):
        super().__init__(name,age)
        
    def gardening(self):
        return "I love gardening."
        
class Son(Father):
    def __init__(self,name,age):
        super().__init__(name,age)
        
    def sports(self):
        return "I enjoy sports."

if __name__ == "__main__":
    dad = Father("John",30)
    son = Son("Jack",5)
    
    print("Father said...",dad.gardening())
    print("Son said...",son.sports() , " and also ", son.gardening())
    print("Age of son is ", son.age)
    print("Age of dad is ", dad.age)            
    