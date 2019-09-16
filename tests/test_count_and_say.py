import unittest
from solutions.count_and_say.solution import Solution


class TestCountAndSay(unittest.TestCase):

    def test_1(self):
        u_input = {
            'n': 1
        }
        u_output = '1'

        solution = Solution()
        u_result = solution.countAndSay(**u_input)
        self.assertEqual(u_output, u_result)

    def test_2(self):
        u_input = {
            'n': 4
        }
        u_output = '1211'

        solution = Solution()
        u_result = solution.countAndSay(**u_input)
        self.assertEqual(u_output, u_result)

    def test_3(self):
        u_input = {
            'n': 14
        }
        u_output = '11131221131211131231121113112221121321132132211331222113112211'

        solution = Solution()
        u_result = solution.countAndSay(**u_input)
        self.assertEqual(u_output, u_result)


if __name__ == '__main__':
    unittest.main()
