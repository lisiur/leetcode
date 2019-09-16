import unittest
from solutions.longest_common_prefix.solution import Solution


class TestLongestCommonPrefix(unittest.TestCase):

    def test_1(self):
        u_input = {
            'strs': ["flower", "flow", "flight"],
        }
        u_output = "fl"

        solution = Solution()
        u_result = solution.longestCommonPrefix(**u_input)
        self.assertEqual(u_output, u_result)

    def test_2(self):
        u_input = {
            'strs': ["dog", "racecar", "car"],
        }
        u_output = ""

        solution = Solution()
        u_result = solution.longestCommonPrefix(**u_input)
        self.assertEqual(u_output, u_result)

    def test_3(self):
        u_input = {
            'strs': ["dog", "dog1", "dog2"],
        }
        u_output = "dog"

        solution = Solution()
        u_result = solution.longestCommonPrefix(**u_input)
        self.assertEqual(u_output, u_result)

    def test_4(self):
        u_input = {
            'strs': ["", "dog1", "dog2"],
        }
        u_output = ""

        solution = Solution()
        u_result = solution.longestCommonPrefix(**u_input)
        self.assertEqual(u_output, u_result)


if __name__ == '__main__':
    unittest.main()
