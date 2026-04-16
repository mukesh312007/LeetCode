class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0

        r = x
        while r > x // r:
            r = (r + x // r) // 2

        return r