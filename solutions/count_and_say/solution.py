class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for i in range(1, n):
            s2 = ''
            j = 0
            while j < len(s):
                c = s[j]
                n = 1
                j += 1
                while j < len(s) and s[j] == c:
                    n += 1
                    j += 1
                s2 = "{s2}{n}{c}".format(s2=s2, n=n, c=c)
            s = s2
        return s
