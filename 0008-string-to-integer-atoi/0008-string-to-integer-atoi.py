class Solution(object):
    def myAtoi(self, s):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i, n = 0, len(s)

        # 1. skip spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. build number
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # overflow check
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num