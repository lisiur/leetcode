import unittest
from solutions.reverse_string.solution import Solution


class TestReverseString(unittest.TestCase):

    def test_1(self):
        u_input = {
            's': ['h', 'e', 'l', 'l', 'o']
        }
        u_output = ['o', 'l', 'l', 'e', 'h']

        solution = Solution()
        solution.reverseString(**u_input)
        self.assertEqual(u_output, u_input['s'])

    def test_2(self):
        u_input = {
            's': ["H", "a", "n", "n", "a", "h"]
        }
        u_output = ["h", "a", "n", "n", "a", "H"]

        solution = Solution()
        solution.reverseString(**u_input)
        self.assertEqual(u_output, u_input['s'])


if __name__ == '__main__':
    unittest.main()
