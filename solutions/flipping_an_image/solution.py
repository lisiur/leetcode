from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            p, q = 0, len(row) - 1
            while p <= q:
                if row[p] == row[q]:
                    row[p] = row[q] = 1 - row[p]
                p, q = p + 1, q - 1
        return A
