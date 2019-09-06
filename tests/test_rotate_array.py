import unittest
from solutions.rotate_array.solution import Solution


class TestRotate(unittest.TestCase):

    def test_1(self):
        u_input = {
            'nums': [1, 2, 3, 4, 5, 6, 7],
            'k': 3,
        }
        u_output = [5, 6, 7, 1, 2, 3, 4]

        solution = Solution()
        solution.rotate(**u_input)
        self.assertEqual(u_output, u_input['nums'])

    def test_2(self):
        u_input = {
            'nums': [-1, -100, 3, 99],
            'k': 2,
        }
        u_output = [3, 99, -1, -100]

        solution = Solution()
        solution.rotate(**u_input)
        self.assertEqual(u_output, u_input['nums'])


if __name__ == '__main__':
    unittest.main()
