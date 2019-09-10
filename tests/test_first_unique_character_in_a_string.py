import unittest
from solutions.first_unique_character_in_a_string.solution import Solution


class TestFirstUniqChar(unittest.TestCase):

    def test_1(self):
        u_input = {
            's': 'leetcode'
        }
        u_output = 0

        solution = Solution()
        u_result = solution.firstUniqChar(**u_input)
        self.assertEqual(u_output, u_result)

    def test_2(self):
        u_input = {
            's': 'loveleetcode'
        }
        u_output = 2

        solution = Solution()
        u_result = solution.firstUniqChar(**u_input)
        self.assertEqual(u_output, u_result)

    def test_3(self):
        u_input = {
            's': ''
        }
        u_output = -1

        solution = Solution()
        u_result = solution.firstUniqChar(**u_input)
        self.assertEqual(u_output, u_result)

    def test_4(self):
        u_input = {
            's': 'cc'
        }
        u_output = -1

        solution = Solution()
        u_result = solution.firstUniqChar(**u_input)
        self.assertEqual(u_output, u_result)


if __name__ == '__main__':
    unittest.main()
