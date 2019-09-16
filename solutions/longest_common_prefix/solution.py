from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ''

        ss = strs[0]
        m = len(ss)
        if m == 0:
            return ''

        p = 0
        while p < m:
            c = ss[p]
            for s in strs[1:]:
                if p >= len(s) or s[p] != c:
                    return ss[:p]
            p += 1
        return ss
