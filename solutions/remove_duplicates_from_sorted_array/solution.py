from typing import List


class Solution:
    def sort(self, nums: List[int]):
        self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self, nums: List[int], start: int, end: int):
        if start >= end:
            return

        base = nums[start]
        p = start
        q = end
        while p < q:
            while p < q and nums[q] > base:
                q -= 1
            nums[p] = nums[q]

            while p < q and nums[p] <= base:
                p += 1
            nums[q] = nums[p]
        nums[p] = base
        self.quick_sort(nums, start, p - 1)
        self.quick_sort(nums, p + 1, end)

    def removeDuplicates(self, nums: List[int]) -> int:
        # self.sort(nums)
        if not nums:
            return 0
        index = 0
        for num in nums:
            if num != nums[index]:
                index += 1
                nums[index] = num
        return index + 1
