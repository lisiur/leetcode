import unittest
from solutions.string_to_integer_atoi.solution import Solution


class TestMyAtoi(unittest.TestCase):

    def test_1(self):
        u_input = {
            'str': '42'
        }
        u_output = 42

        solution = Solution()
        u_result = solution.myAtoi(**u_input)
        self.assertEqual(u_output, u_result)

    def test_2(self):
        u_input = {
            'str': '    -42'
        }
        u_output = -42

        solution = Solution()
        u_result = solution.myAtoi(**u_input)
        self.assertEqual(u_output, u_result)

    def test_3(self):
        u_input = {
            'str': '4193 with words'
        }
        u_output = 4193

        solution = Solution()
        u_result = solution.myAtoi(**u_input)
        self.assertEqual(u_output, u_result)

    def test_4(self):
        u_input = {
            'str': 'words and 987'
        }
        u_output = 0

        solution = Solution()
        u_result = solution.myAtoi(**u_input)
        self.assertEqual(u_output, u_result)

    def test_5(self):
        u_input = {
            'str': '-91283472332'
        }
        u_output = -2147483648

        solution = Solution()
        u_result = solution.myAtoi(**u_input)
        self.assertEqual(u_output, u_result)

    def test_6(self):
        u_input = {
            'str': '   -a'
        }
        u_output = 0

        solution = Solution()
        u_result = solution.myAtoi(**u_input)
        self.assertEqual(u_output, u_result)

    def test_7(self):
        u_input = {
            'str': ''
        }
        u_output = 0

        solution = Solution()
        u_result = solution.myAtoi(**u_input)
        self.assertEqual(u_output, u_result)

    def test_8(self):
        u_input = {
            'str': '+1'
        }
        u_output = 1

        solution = Solution()
        u_result = solution.myAtoi(**u_input)
        self.assertEqual(u_output, u_result)

    def test_9(self):
        u_input = {
            'str': "  0000000000012345678"
        }
        u_output = 12345678

        solution = Solution()
        u_result = solution.myAtoi(**u_input)
        self.assertEqual(u_output, u_result)


if __name__ == '__main__':
    unittest.main()
