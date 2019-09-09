import unittest
from solutions.valid_sudoku.solution import Solution


class TestIsValidSudoku(unittest.TestCase):

    def test_1(self):
        u_input = {
            'board': [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]
            ],

        }
        u_output = True

        solution = Solution()
        u_result = solution.isValidSudoku(**u_input)
        self.assertEqual(u_output, u_result)

    def test_2(self):
        u_input = {
            'board': [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]
            ],
        }
        u_output = False

        solution = Solution()
        u_result = solution.isValidSudoku(**u_input)
        self.assertEqual(u_output, u_result)


if __name__ == '__main__':
    unittest.main()
