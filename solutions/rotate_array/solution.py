from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums:
            return

        k = k % len(nums)
        times = 0
        start = 0

        while times < len(nums):
            prev = nums[start]
            current = (start + k) % len(nums)
            while current != start:
                nums[current], prev = prev, nums[current]
                current = (current + k) % len(nums)
                times += 1
            else:
                nums[current] = prev
                start += 1
                times += 1



