# Problem: Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and
# return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
# extra memory.
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    iter = 0
    track = 0
    duplicate = 1
    try:
        for idx, val in enumerate(nums):
            duplicate = 1
            if val == nums[iter+1] and duplicate==2:
                nums.pop(iter+1)
        if duplicate > 2:
            duplicate = 2
        print(idx)
        print('add', duplicate)
        res += duplicate
    except:
        print('Break here')
        print(idx)

    return res
        # finally:
        #     if nums[-1] == nums[-2]:
        #         return res
        #     else:
        #         return res + 1

nums = [1,1,1,2,2,3]

removeDuplicates(nums)

# Solution:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n

        a = 0
        # since it is allowed to have at most 2 duplicates, b starts at 2
        b = 2
        # If b == n, break and return a + 2
        while b < n:
            # compare current value at index b with a
            # add 1 to b if conditions hold
            #
            while b < n and nums[b] == nums[a]:
                b += 1
            # if after iterating through all the values in the list
            # the number stays the same, break and return a + 2
            if b == n:
                break
            # if a new number shows up, remove the duplicates that exceeds twice
            # move both a, b by 1 to the left
            nums[a + 2] = nums[b]
            a += 1
            b += 1

        return a + 2