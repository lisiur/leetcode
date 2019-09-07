from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        non_zero = 0
        n = len(nums)
        while True:
            while zero < n and nums[zero] != 0:
                zero += 1
            if zero >= n:
                return

            non_zero = max(zero + 1, non_zero)
            while non_zero < n and nums[non_zero] == 0:
                non_zero += 1

            if non_zero >= n:
                return

            nums[non_zero], nums[zero] = nums[zero], nums[non_zero]
            zero += 1

    def moveZeroes2(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0
