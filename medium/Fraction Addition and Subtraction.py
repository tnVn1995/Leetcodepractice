import numpy as np
from fractions import Fraction


# Problem: Given a string representing an expression of fraction addition and subtraction, you need to return the
# calculation result in string format. The final result should be irreducible fraction. If your final result is an
# integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case,
# 2 should be converted to 2/1.

# My answer

def fractionAddition(expression: str) -> str:
    operations = {'-': np.subtract, '+': np.add}
    # Check if there is sign at the start
    # and assign the first sign to minusadd
    res = 0
    if expression[0] != '+':
        res = operations['+'](res, Fraction(int(expression[1]), int(expression[3])))
    else:
        res = operations['-'](res, Fraction(int(expression[1]), int(expression[3])))

    for idx, val in enumerate(expression):
        if idx == 0:
            pass
        elif expression[idx] in operations.keys():
            try:
                res = operations[val](res, Fraction(int(expression[(idx + 1)]), int(expression[(idx + 3)])))
            except:
                print('There\'s an error here')
                print('Check index\t', idx)
    if str(res).isnumeric():
        return str(res) + '/1'
    return str(res)
## Result: Wrong

# %%
# np.add(1,2)
# np.subtract(1,2)
# operations = {'-': np.subtract, '+': np.add, '/': np.divide}
# operations = {'-': np.subtract, '+': np.add}
# idx = 4
# expression = "-1/2+1/2"
# res = 0
# res = operations[expression[idx]](res, Fraction(int(expression[(idx + 1)]), int(expression[(idx + 3)])))
# fractionAddition(expression)
#
# for idx, val in enumerate(expression):
#     if idx == 0 or idx == 1:
#         pass
#     elif expression[idx] in operations.keys():
#         print(idx)


# User's Submission
import math
class Solution:
    def fractionAddition(self, f: str) -> str:
        f, d = [int(i) for i in (f.replace('/', ' ').replace('+', ' +').replace('-', ' -')).split()], 1
        for i in range(1, len(f), 2): d *= f[i]
        return (lambda x, y: str(x // math.gcd(x, y)) + "/" + str(y // math.gcd(x, y)))(
            sum(d * f[i] // f[i + 1] for i in range(0, len(f), 2)), d)

# Result:Runtime: 28 ms, faster than 72.50% of Python3 online submissions for Fraction Addition and Subtraction.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Fraction Addition and Subtraction
