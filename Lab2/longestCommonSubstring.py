# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:58:25 2023

@author: TORA TECH
"""
def LongestCommonString(string1, string2):
    """Length of strings"""
    m = len(string1)
    n = len(string2)

    list2d = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                list2d[i][j] = list2d[i - 1][j - 1] + 1
            else:
                list2d[i][j] = max(list2d[i - 1][j], list2d[i][j - 1])

    a = list2d[m][n]
    """Length of string"""
    b = [""] * a
    i, j = m, n

    while i > 0 and j > 0:
        if string1[i - 1] == string2[j - 1]:
            b[a - 1] = string1[i - 1]
            i = i - 1
            j = j - 1
            a = a - 1
        elif list2d[i - 1][j] > list2d[i][j - 1]:
            i -= 1
        else:
            j -= 1
    result = "".join(b)

    return result


string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

print("Longest Common Substring is: ", LongestCommonString(string1, string2))