##
from typing import List
import numpy as np
from collections import Counter


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        """reconstruct a 2-row binary matrix from upper, lower and colsum"""
        cols = len(colsum)  # The number of columns of the matrix equals the length of colsum
        res = [[0]*cols, [0]*cols]
        if upper + lower != np.sum(np.array(colsum)) or colsum.count(2) > min(upper,lower):
            return []
        twos = Counter(colsum)[2]
        for idx, val in enumerate(colsum):
            if val == 2:
                res[0][idx] = 1
                res[1][idx] = 1
                twos -= 1
                upper -= 1
                lower -= 1
        for idx, val in enumerate(colsum):
            if val == 1:
                if upper > twos:
                    res[0][idx] = 1
                    res[1][idx] = 0
                    upper -= 1
                else:
                    res[1][idx] = 1
                    res[0][idx] = 0
        return res


# print(np.array([2,1,2,0,1,0,1,2,0,1]))
# print(np.array([[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]))
##
x = [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]
upper = 2
lower = 3
colsum = [2, 2, 1, 1]
sol = Solution()
sol.reconstructMatrix(upper=upper, lower=lower, colsum=colsum)
##
upper = 5
lower = 5
colsum = [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]
sol = Solution()
a = sol.reconstructMatrix(upper=upper, lower=lower, colsum=colsum)
a = np.array(a)
assert np.array_equal(np.sum(a,axis=1), np.array([upper,lower])), 'Wrong!'
assert np.array_equal(np.sum(a, axis=0), np.array(colsum)), 'Wrong!!'
##
upper = 2
lower = 1
colsum = [1,1,1]
sol = Solution()
a = sol.reconstructMatrix(upper=upper, lower=lower, colsum=colsum)
a = np.array(a)
assert np.array_equal(np.sum(a,axis=1), np.array([upper,lower])), 'Wrong!'
assert np.array_equal(np.sum(a, axis=0), np.array(colsum)), 'Wrong!!'

# Result : Runtime: 848 ms, faster than 10.57% of Python3 online submissions for Reconstruct a 2-Row Binary Matrix.
# Memory Usage: 38.7 MB, less than 100.00% of Python3 online submissions for Reconstruct a 2-Row Binary Matrix.

##
class Solution:
    def reconstructMatrix(self, U: int, L: int, C: List[int]) -> List[List[int]]:
        M, u = [[0]*len(C) for _ in range(2)], C.count(2)
        if U + L != sum(C) or u > min(L,U): return []
        for j,s in enumerate(C):
            if s == 2: M[0][j] = M[1][j] = 1
        for j,s in enumerate(C):
            if s == 1:
                if u < U: M[0][j], u = 1, u + 1
                else: M[1][j] = 1
        return M