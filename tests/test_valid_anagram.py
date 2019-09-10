import unittest
from solutions.valid_anagram.solution import Solution


class TestIsAnagram(unittest.TestCase):

    def test_1(self):
        u_input = {
            's': 'anagram',
            't': 'nagaram',
        }
        u_output = True

        solution = Solution()
        u_result = solution.isAnagram(**u_input)
        self.assertEqual(u_output, u_result)

    def test_2(self):
        u_input = {
            's': 'rat',
            't': 'car',
        }
        u_output = False

        solution = Solution()
        u_result = solution.isAnagram(**u_input)
        self.assertEqual(u_output, u_result)

    def test_3(self):
        u_input = {
            's': '',
            't': '',
        }
        u_output = True

        solution = Solution()
        u_result = solution.isAnagram(**u_input)
        self.assertEqual(u_output, u_result)


if __name__ == '__main__':
    unittest.main()
