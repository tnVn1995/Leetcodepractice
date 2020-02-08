# Problem: Given an array nums of integers, return how many of them contain an even number of digits.
from typing import List


def findNumbers(num: List[int]) -> int:
    num = [str(x) for x in num]
    res = 0
    for i in num:
        if len(i) % 2 == 0:
            res += 1
    return res


list = [12, 345, 2, 6, 7896]

findNumbers(list)

# Result: Runtime: 48 ms, faster than 91.81% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Numbers with Even Number of Digits.
