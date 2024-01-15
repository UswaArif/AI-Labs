# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:22:07 2023

@author: TORA TECH
"""

def BalanceBrackets(s):
    count1 = 0
    count2 = 0
    
    for char in s:
        if char == '(':
            count1 = count1 + 1
        elif char == ')':
            if count1 == 0:
                count2 = count2 + 1
            else:
                count1 = count1 - 1
    
    balancedString = '('*count2 + s + ')'*count1
    
    return balancedString

s = input("Enter the string: ")
print("The balanced bracket sequence is: ", BalanceBrackets(s))


