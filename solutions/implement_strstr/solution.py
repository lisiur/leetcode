class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        if m == 0:
            return 0
        n = len(haystack)
        if n == 0:
            return -1
        next_arr = self.get_next(needle)
        i = 0
        j = 0
        while j != m:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - j
                if i == n:
                    return -1
            else:
                j = next_arr[j]

    def get_next(self, s: str,):
        next_arr = [-1] * len(s)
        for i in range(1, len(s)):
            k = i - 1
            while k > 0:
                if s[next_arr[k]] == s[i-1]:
                    next_arr[i] = next_arr[k] + 1
                    break
                else:
                    k = next_arr[k]
            else:
                next_arr[i] = 0

        return next_arr
