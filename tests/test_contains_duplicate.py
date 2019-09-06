import unittest
from solutions.contains_duplicate.solution import Solution


class TestContainsDuplicate(unittest.TestCase):

    def test_1(self):
        u_input = {
            'nums': [1, 2, 3, 1],
        }
        u_output = True

        solution = Solution()
        u_result = solution.containsDuplicate(**u_input)
        self.assertEqual(u_output, u_result)

    def test_2(self):
        u_input = {
            'nums': [1, 2, 3, 4],
        }
        u_output = False

        solution = Solution()
        u_result = solution.containsDuplicate(**u_input)
        self.assertEqual(u_output, u_result)

    def test_3(self):
        u_input = {
            'nums': [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
        }
        u_output = True

        solution = Solution()
        u_result = solution.containsDuplicate(**u_input)
        self.assertEqual(u_output, u_result)


if __name__ == '__main__':
    unittest.main()
