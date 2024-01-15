# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:32:11 2023

@author: TORA TECH
"""

def fibonacci(num):
    """Length of array"""
    array = [0] * (num + 1)
    array[0] = 0
    array[1] = 1
    for i in range(2, num + 1):
        array[i] = array[i - 1] + array[i - 2]
    return array[num]

num = input("Enter a Number: ")
print(fibonacci(int(num)))