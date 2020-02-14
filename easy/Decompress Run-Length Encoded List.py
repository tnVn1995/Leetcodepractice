# Problem: You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
#  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, 
# so "a" is considered a different type of stone from "A".


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0
        for val in J:
            res += list(S).count(val)
        return res

# Result: Runtime: 24 ms, faster than 90.12% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Jewels and Stones.


if __name__ == "__main__":
    J = "z"
    S = "ZZ"
    sol = Solution()
    print(sol.numJewelsInStones(J,S))
    
