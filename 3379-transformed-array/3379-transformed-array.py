class Solution(object):
    def constructTransformedArray(self, nums):
        n = len(nums)
        res = [0] * n

        for i in range(n):
            if nums[i] > 0:
                j = (i + nums[i]) % n
                res[i] = nums[j]
            elif nums[i] < 0:
                j = (i - abs(nums[i])) % n
                res[i] = nums[j]
            else:
                res[i] = 0

        return res