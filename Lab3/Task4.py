# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:53:35 2023

@author: TORA TECH
"""

def CoinsProblem(coins, amount):
    INF = float('inf')
    #2d array
    array2d = [INF] * (amount + 1)
    
    #For zero coins
    array2d[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                array2d[i] = min(array2d[i], array2d[i - coin] + 1)

    return array2d[amount]


# Taking input for the Coin Counts
Coin_Count = int(input("Enter the Number of Coins: "))
coins = []
# Taking input for the coins
for i in range(Coin_Count):
    n = int(input(f"Enter Coins {i + 1}: "))
    coins.append(n)
    
# Taking input for the amount
amount = int(input("Enter the target amount: "))
print(CoinsProblem(coins, amount))