from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        cp_digits = digits[:]
        for i in range(n-1, -1, -1):
            if cp_digits[i] < 9:
                cp_digits[i] += 1
                return cp_digits
            cp_digits[i] = 0

        cp_digits = [0 for i in range(n + 1)]
        cp_digits[0] = 1

        return cp_digits
