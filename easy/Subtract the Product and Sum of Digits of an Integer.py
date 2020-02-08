# Problem Statement: Given an integer number n, return the difference between the product of its digits and the sum
# of its digits.

def subtractProductAndSum(self, n: int) -> int:
    no_list = str(n)
    product = 1
    sums = 0
    for idx, val in enumerate(no_list):
        product *= int(val)
        sums += int(val)
    return product - sums

# Result: Runtime: 24 ms, faster than 84.89% of Python3 online submissions for Subtract the Product and Sum of Digits
# of an Integer. Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Subtract the Product and
# Sum of Digits of an Integer.
