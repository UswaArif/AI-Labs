# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 13:52:27 2023

@author: TORA TECH
"""
def Edit_Distance(string1, string2):
    #Lengths of strings
    length1 = len(string1)
    length2 = len(string2)
    
    #Creating 2d array 
    array2d = [[0] * (length2 + 1) for _ in range(length1 + 1)]

    for i in range(length1 + 1):
        array2d[i][0] = i
        
    for j in range(length2 + 1):
        array2d[0][j] = j

    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            if string1[i - 1] == string2[j - 1]:
                array2d[i][j] = array2d[i - 1][j - 1]
            else:
                insertion = array2d[i - 1][j]
                deletion = array2d[i][j - 1]
                substitution = array2d[i - 1][j - 1]
                array2d[i][j] = 1 + min(insertion, deletion, substitution)

    return array2d[length1][length2]

string1 = input("Enter String 1: ")
string2 = input("Enter String 2: ")

distance = Edit_Distance(string1, string2)
print(distance)
