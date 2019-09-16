import unittest
from solutions.implement_strstr.solution import Solution


class TestStrStr(unittest.TestCase):

    def test_1(self):
        u_input = {
            'haystack': 'hello',
            'needle': 'll'
        }
        u_output = 2

        solution = Solution()
        u_result = solution.strStr(**u_input)
        self.assertEqual(u_output, u_result)

    def test_2(self):
        u_input = {
            'haystack': 'aaaaa',
            'needle': 'bba'
        }
        u_output = -1

        solution = Solution()
        u_result = solution.strStr(**u_input)
        self.assertEqual(u_output, u_result)

    def test_3(self):
        u_input = {
            'haystack': 'aaaaa',
            'needle': ''
        }
        u_output = 0

        solution = Solution()
        u_result = solution.strStr(**u_input)
        self.assertEqual(u_output, u_result)

    def test_4(self):
        u_input = {
            'haystack': 'aaaaa',
            'needle': 'a'
        }
        u_output = 0

        solution = Solution()
        u_result = solution.strStr(**u_input)
        self.assertEqual(u_output, u_result)

    def test_5(self):
        u_input = {
            'haystack': 'a',
            'needle': 'a'
        }
        u_output = 0

        solution = Solution()
        u_result = solution.strStr(**u_input)
        self.assertEqual(u_output, u_result)


if __name__ == '__main__':
    unittest.main()
