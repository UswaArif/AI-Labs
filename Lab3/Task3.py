# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:33:32 2023

@author: TORA TECH
"""

def Sequence_Alignment(s1, s2, matchs, mismatch, gap):
    #Lengths of sequences
    length1 = len(s1)
    length2 = len(s2)
    
    #Creating 2d Array
    array2d = [[0] * (length2 + 1) for _ in range(length1 + 1)]
    
    for i in range(length1 + 1):
        array2d[i][0] = i * gap
    for j in range(length2 + 1):
        array2d[0][j] = j * gap

    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            matchs = array2d[i - 1][j - 1] + (matchs if s1[i - 1] == s2[j - 1] else mismatch)
            delete = array2d[i - 1][j] + gap
            insert = array2d[i][j - 1] + gap
            
            # Maximum scores
            array2d[i][j] = max(matchs, delete, insert)
    
    # Backtracking
    alignment1 = []
    alignment2 = []
    i = length1
    j = length2
    while i > 0 or j > 0:
        scores = array2d[i][j]
        if i > 0 and array2d[i - 1][j] + gap == scores:
            alignment1.insert(0, s1[i - 1])
            alignment2.insert(0, '-')
            i = i - 1
        elif j > 0 and array2d[i][j - 1] + gap == scores:
            alignment1.insert(0, '-')
            alignment2.insert(0, s2[j - 1])
            j = j - 1
        else:
            alignment1.insert(0, s1[i - 1])
            alignment2.insert(0, s2[j - 1])
            i = i - 1
            j = j - 1
    
    return array2d[length1][length2], ''.join(alignment1), ''.join(alignment2)

#Taking Input of Sequences
s1 = input("Enter the sequence of DNA as String 1: ")
s2 = input("Enter the sequence of DNA as String 2: ")

matchs = 1
mismatch = -1
gap = -2

result = Sequence_Alignment(s1, s2, matchs, mismatch, gap)
score = result[0]
alignment1 = result[1]
alignment2 = result[2]

print("The Alignment Score is:", score)
print("Alignment 1:", alignment1)
print("Alignment 2:", alignment2)