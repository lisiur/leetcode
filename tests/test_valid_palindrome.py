import unittest
from solutions.valid_palindrome.solution import Solution


class TestIsPalindrome(unittest.TestCase):

    def test_1(self):
        u_input = {
            's': 'A man, a plan, a canal: Panama'
        }
        u_output = True

        solution = Solution()
        u_result = solution.isPalindrome(**u_input)
        self.assertEqual(u_output, u_result)

    def test_2(self):
        u_input = {
            's': 'race a car'
        }
        u_output = False

        solution = Solution()
        u_result = solution.isPalindrome(**u_input)
        self.assertEqual(u_output, u_result)

    def test_3(self):
        u_input = {
            's': ''
        }
        u_output = True

        solution = Solution()
        u_result = solution.isPalindrome(**u_input)
        self.assertEqual(u_output, u_result)

    def test_4(self):
        u_input = {
            's': '"`l;`` 1o1 ??;l`"'
        }
        u_output = True

        solution = Solution()
        u_result = solution.isPalindrome(**u_input)
        self.assertEqual(u_output, u_result)


if __name__ == '__main__':
    unittest.main()
