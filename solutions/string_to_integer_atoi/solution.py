class Solution:
    def is_larger(self, a: str, b: str):
        if len(a) == len(b):
            return a > b
        else:
            return len(a) > len(b)

    def is_number(self, c: str) -> bool:
        return 48 <= ord(c) <= 57

    def valid_start(self, c: str) -> bool:
        return self.is_number(c) or c == '-' or c == '+'

    def myAtoi(self, str: str) -> int:
        n = len(str)
        sign = 1
        i = 0

        while i < n and not self.valid_start(str[i]):
            if str[i] == ' ':
                i += 1
            else:
                return 0

        if i >= n:
            return 0

        if str[i] == '-':
            sign = -1
            i += 1
        elif str[i] == '+':
            i += 1

        while i < n and str[i] == '0':  # 跳过 0
            i += 1

        j = i

        while j < n and self.is_number(str[j]):
            j += 1

        if i == j:  # 只有 '-'
            return 0

        valid_str = str[i:j]

        if sign == 1 and self.is_larger(valid_str, '2147483647'):
            return 2147483647

        if sign == -1 and self.is_larger(valid_str, '2147483648'):
            return -2147483648

        r = 0
        for c in valid_str:
            r = r * 10 + ord(c) - 48

        return r * sign
