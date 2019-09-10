class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}

        for i, c in enumerate(s):
            d[c] = d[c] + 1 if c in d else 1

        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1
