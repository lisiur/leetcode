class Solution:
    def isPalindrome(self, s: str) -> bool:
        def validChar(c) -> bool:
            o = ord(c)
            return ord('0') <= o <= ord('9') or ord('a') <= o <= ord('z')

        s = [c for c in s.lower() if validChar(c)]
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
