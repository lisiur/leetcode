import unittest
from solutions.single_number.solution import Solution


class TestSingleNumber(unittest.TestCase):

    def test_1(self):
        u_input = {
            'nums': [2, 2, 1],
        }
        u_output = 1

        solution = Solution()
        u_result = solution.singleNumber(**u_input)
        self.assertEqual(u_output, u_result)

    def test_2(self):
        u_input = {
            'nums': [4, 1, 2, 1, 2],
        }
        u_output = 4

        solution = Solution()
        u_result = solution.singleNumber(**u_input)
        self.assertEqual(u_output, u_result)


if __name__ == '__main__':
    unittest.main()
