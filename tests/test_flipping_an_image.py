import unittest
from solutions.flipping_an_image.solution import Solution


class TestFlipAndInvertImage(unittest.TestCase):

    def test_1(self):
        u_input = {
            'A': [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
        }
        u_output = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

        solution = Solution()
        u_result = solution.flipAndInvertImage(**u_input)
        self.assertEqual(u_result, u_output)


if __name__ == '__main__':
    unittest.main()
