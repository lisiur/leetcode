import unittest
from solutions.remove_duplicates_from_sorted_array.solution import Solution


class TestRemoveDuplicates(unittest.TestCase):

    def test_1(self):
        u_input = {
        }
        u_output = ()

        solution = Solution()
        u_result = solution.removeDuplicates(**u_input)
        self.assertEqual(u_result, u_output)


if __name__ == '__main__':
    unittest.main()
