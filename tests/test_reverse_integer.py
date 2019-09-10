import unittest
from solutions.reverse_integer.solution import Solution


class TestReverse(unittest.TestCase):

    def test_1(self):
        u_input = {
            'x': 123
        }
        u_output = 321

        solution = Solution()
        u_result = solution.reverse(**u_input)
        self.assertEqual(u_output, u_result)

    def test_2(self):
        u_input = {
            'x': -123
        }
        u_output = -321

        solution = Solution()
        u_result = solution.reverse(**u_input)
        self.assertEqual(u_output, u_result)

    def test_3(self):
        u_input = {
            'x': 120
        }
        u_output = 21

        solution = Solution()
        u_result = solution.reverse(**u_input)
        self.assertEqual(u_output, u_result)

    def test_3(self):
        u_input = {
            'x': 1534236469
        }
        u_output = 0

        solution = Solution()
        u_result = solution.reverse(**u_input)
        self.assertEqual(u_output, u_result)

    def test_4(self):
        u_input = {
            'x': 0
        }
        u_output = 0

        solution = Solution()
        u_result = solution.reverse(**u_input)
        self.assertEqual(u_output, u_result)


if __name__ == '__main__':
    unittest.main()
