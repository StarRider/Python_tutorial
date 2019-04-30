#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:52:20 2019

@author: sharon
"""

'''
Human       Fighter
    \       /
     \     /
     Student
     
multiple inheritance
'''

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Fighter:
    def __init__(self,style):
        self.style = style
        
class Student(Human,Fighter):
    def __init__(self,name,age,style):
        # Notice we passed self here because init is an instance method.
        Human.__init__(self,name,age)
        Fighter.__init__(self,style)

    def __repr__(self):
        return self.name + " is a " + str(self.age) + "yr old " + self.style + " fighter."

if __name__ == "__main__":
    shojo = Student("Shojo", 22, "Kung fu")
    print(shojo)