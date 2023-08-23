#!/usr/bin/python3
''' determining the fewest number of coins needed to meet a given amount total '''

def makeChange(coins, total):
    ''' Return fewest number of coins '''
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)
    addition = 0
    a = 0
    count = 0
    no_of_coins = len(coins)
    while addition < total and a < no_of_coins:
        while coins[a] <= total - addition:
            addition += coins[a]
            count += 1
            if addition == total:
                return count
        a += 1
    return -1
