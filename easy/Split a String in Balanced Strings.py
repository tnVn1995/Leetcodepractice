# Problem: Balanced strings are those who have equal quantity of 'L' and 'R' characters.
#
# Given a balanced string s split it in the maximum amount of balanced strings.
#
# Return the maximum amount of splitted balanced strings.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        l = 0
        sub = 0
        for char in s:
            if char == 'R':
                r += 1
            else:
                l += 1
            if r != 0 and r == l:
                sub += 1
                r = 0
                l = 0
        return sub

sol = Solution()

string = "RLRRLLRLRL"
string = 'RLLLLRRRLR'
s = 'LLLLRRRR'
sol.balancedStringSplit(s)

# Results: Runtime: 28 ms, faster than 69.22% of Python3 online submissions for Split a String in Balanced Strings.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Split a String in Balanced Strings.

