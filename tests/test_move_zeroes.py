import unittest
from solutions.move_zeroes.solution import Solution


class TestMoveZeroes(unittest.TestCase):

    def test_1(self):
        u_input = {
            'nums': [0, 1, 0, 3, 12],
        }
        u_output = [1, 3, 12, 0, 0]

        solution = Solution()
        solution.moveZeroes2(**u_input)
        self.assertEqual(u_output, u_input['nums'])

    def test_2(self):
        u_input = {
            'nums': [],
        }
        u_output = []

        solution = Solution()
        solution.moveZeroes2(**u_input)
        self.assertEqual(u_output, u_input['nums'])

    def test_3(self):
        u_input = {
            'nums': [1, 0],
        }
        u_output = [1, 0]

        solution = Solution()
        solution.moveZeroes2(**u_input)
        self.assertEqual(u_output, u_input['nums'])

    def test_4(self):
        u_input = {
            'nums': [1, 0, 1],
        }
        u_output = [1, 1, 0]

        solution = Solution()
        solution.moveZeroes2(**u_input)
        self.assertEqual(u_output, u_input['nums'])


if __name__ == '__main__':
    unittest.main()
