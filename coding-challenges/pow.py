# Implement pow(x, n), which calculates x raised to the power n(x^n)

# Example:
# Input: 2.00000, 10
# Output: 1024.0`0000

import math

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return math.pow(x, n)
        