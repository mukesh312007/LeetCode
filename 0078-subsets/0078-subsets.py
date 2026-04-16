class Solution(object):
    def subsets(self, nums):
        res = [[]]

        for num in nums:
            res += [curr + [num] for curr in res]

        return res