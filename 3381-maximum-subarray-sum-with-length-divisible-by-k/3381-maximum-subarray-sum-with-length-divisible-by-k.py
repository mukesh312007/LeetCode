class Solution(object):
    def maxSubarraySum(self, nums, k):
        prefix = 0
        res = float('-inf')
        
        min_prefix = {0: 0}
        
        for i, num in enumerate(nums, 1):
            prefix += num
            r = i % k
            
            if r in min_prefix:
                res = max(res, prefix - min_prefix[r])
                min_prefix[r] = min(min_prefix[r], prefix)
            else:
                min_prefix[r] = prefix
        
        return res