class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)

        def inc(l, r):
            for i in range(l + 1, r + 1):
                if nums[i] <= nums[i - 1]:
                    return False
            return True

        def dec(l, r):
            for i in range(l + 1, r + 1):
                if nums[i] >= nums[i - 1]:
                    return False
            return True

        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                if inc(0, p) and dec(p, q) and inc(q, n - 1):
                    return True

        return False