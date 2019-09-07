import unittest
from solutions.plus_one.solution import Solution


class TestPlusOne(unittest.TestCase):

    def test_1(self):
        u_input = {
            'digits': [1, 2, 3],
        }
        u_output = [1, 2, 4]

        solution = Solution()
        u_result = solution.plusOne(**u_input)
        self.assertEqual(u_output, u_result)

    def test_2(self):
        u_input = {
            'digits': [4, 3, 2, 1],
        }
        u_output = [4, 3, 2, 2]

        solution = Solution()
        u_result = solution.plusOne(**u_input)
        self.assertEqual(u_output, u_result)


if __name__ == '__main__':
    unittest.main()
