#!/usr/bin/python3
""" Prime Game """

def isWinner(x, nums):
    """Prime Game Solution"""
    if not nums or x < 1:
        return None
    a = max(nums)
    sort = [True for _ in range(max(a + 1, 2))]
    for e in range(2, int(pow(a, 0.5)) + 1):
        if not sort[e]:
            continue
        for f in range(e*e, a + 1, e):
            sort[f] = False

    sort[0] = sort[1] = False
    b = 0
    for e in range(len(sort)):
        if sort[e]:
            b += 1
        sort[e] = b

    First_player = 0
    for a in nums:
        First_player += sort[a] % 2 == 1
    if First_player * 2 == len(nums):
        return None
    if First_player * 2 > len(nums):
        return "Maria"
    return "Ben"
