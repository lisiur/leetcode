from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        p1 = 0
        p2 = 0
        result = []
        while True:
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1

            elif nums1[p1] > nums2[p2]:
                p2 += 1

            else:
                p1 += 1

            if p1 == len(nums1) or p2 == len(nums2):
                break

        return result
