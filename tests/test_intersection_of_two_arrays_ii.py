import unittest
from solutions.intersection_of_two_arrays_ii.solution import Solution


class TestIntersect(unittest.TestCase):

    def test_1(self):
        u_input = {
            'nums1': [1, 2, 2, 1],
            'nums2': [2, 2],
        }
        u_output = [2, 2]

        solution = Solution()
        u_result = solution.intersect(**u_input)
        u_result.sort()
        self.assertEqual(u_output, u_result)

    def test_2(self):
        u_input = {
            'nums1': [4, 9, 5],
            'nums2': [9, 4, 9, 8, 4],
        }
        u_output = [4, 9]

        solution = Solution()
        u_result = solution.intersect(**u_input)
        u_result.sort()
        self.assertEqual(u_output, u_result)


if __name__ == '__main__':
    unittest.main()
