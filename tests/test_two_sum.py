import unittest
from solutions.two_sum.solution import Solution


class TestTwoSum(unittest.TestCase):

    def test_1(self):
        u_input = {
            'nums': [2, 7, 11, 15],
            'target': 9,
        }
        u_output = [0, 1]

        solution = Solution()
        u_result = solution.twoSum(**u_input)
        self.assertEqual(u_output, u_result)


if __name__ == '__main__':
    unittest.main()
