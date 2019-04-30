#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:39:23 2019

@author: sharon
"""

class Father:        
    def gardening(self):
        return "I love gardening."
    def common(self):
        return "I am a man."
        
class Mother:
    def cooking(self):
        return "I love cooking!"
    def common(self):
        return "I am a woman."
    
class Son(Father, Mother):    
    def sports(self):
        return "I enjoy sports."
#   # Uncomment and Comment this to see the change
#    def common(self):
        # overriding the parent function
#        return Mother.common(self)
        
if __name__ == "__main__":
    son = Son()
    print("Son said...",son.cooking()," and ", son.gardening(), " and ", son.sports())

    # see if common function is used then the comman function of Father is used.
    print("Son said...",son.common())
    
    