class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == '' and t == '':
            return True
        if s == '' or t == '':
            return False
        d = {}
        for c in s:
            d[c] = d[c] + 1 if c in d else 1
        for c in t:
            if c in d:
                d[c] = d[c] - 1
                if d[c] == -1:
                    return False
            else:
                return False
        return max(d.values()) == 0
