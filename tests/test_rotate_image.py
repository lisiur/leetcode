import unittest
from solutions.rotate_image.solution import Solution


class TestRotate(unittest.TestCase):

    def test_1(self):
        u_input = {
            'matrix': [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
        }
        u_output = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]

        solution = Solution()
        solution.rotate(**u_input)
        self.assertEqual(u_output, u_input['matrix'])

    def test_2(self):
        u_input = {
            'matrix': [
                [5, 1, 9, 11],
                [2, 4, 8, 10],
                [13, 3, 6, 7],
                [15, 14, 12, 16]
            ],
        }
        u_output = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ]

        solution = Solution()
        solution.rotate(**u_input)
        self.assertEqual(u_output, u_input['matrix'])


if __name__ == '__main__':
    unittest.main()
