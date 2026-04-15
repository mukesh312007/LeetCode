class Solution(object):
    def addBinary(self, a, b):
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            x = ord(a[i]) - ord('0') if i >= 0 else 0
            y = ord(b[j]) - ord('0') if j >= 0 else 0

            total = x + y + carry
            res.append(str(total % 2))
            carry = total // 2

            i -= 1
            j -= 1

        return ''.join(res[::-1])