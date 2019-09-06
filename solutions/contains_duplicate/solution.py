from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if d.get(i):
                return True
            d[i] = True
        return False
