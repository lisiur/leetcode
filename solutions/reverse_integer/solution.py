class Solution:

    def larger(self, a: str, b: str):
        if len(a) > len(b):
            return True
        elif len(a) < len(b):
            return False
        else:
            return a > b

    def reverse(self, x: int) -> int:
        maxN = '2147483647'

        if x == -2147483648:  # 把边界条件剔除,则后面 x = -x 是安全的操作
            return 0

        sign = 1 if x >= 0 else -1
        x = sign * x

        s = str(x)[::-1]
        if self.larger(s, maxN):
            return 0
        else:
            return sign * int(s)
