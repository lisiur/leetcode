from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d_row = [{} for i in range(9)]
        d_col = [{} for i in range(9)]
        d_square = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                row = d_row[i]
                col = d_col[j]
                square = d_square[j//3 * 3 + i // 3]
                cell = board[i][j]

                if cell == '.':
                    continue

                if cell in row:
                    return False
                else:
                    row[cell] = True

                if cell in col:
                    return False
                else:
                    col[cell] = True

                if cell in square:
                    return False
                else:
                    square[cell] = True
        return True
