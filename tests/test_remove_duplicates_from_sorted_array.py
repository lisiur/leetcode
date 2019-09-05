import unittest
from solutions.remove_duplicates_from_sorted_array.solution import Solution


class TestRemoveDuplicates(unittest.TestCase):

    def test_1(self):
        u_input = {
            'nums': [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        }
        u_output = 5

        solution = Solution()
        u_result = solution.removeDuplicates(**u_input)
        self.assertEqual(u_result, u_output)

    def test_sort(self):
        u_input = {
            'nums': [2, 5, 6, 8, 2, 1, 9],
        }
        u_output = [1, 2, 2, 5, 6, 8, 9]

        solution = Solution()
        solution.sort(**u_input)
        u_result = u_input['nums']
        self.assertEqual(u_result, u_output)


if __name__ == '__main__':
    unittest.main()
