from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d: Dict[int, int] = {}
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            else:
                d[target-num] = i
        return []
