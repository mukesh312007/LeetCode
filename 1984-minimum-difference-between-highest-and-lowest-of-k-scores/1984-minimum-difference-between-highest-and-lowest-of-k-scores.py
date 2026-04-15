class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        
        ans = float('inf')
        
        for i in range(len(nums) - k + 1):
            ans = min(ans, nums[i + k - 1] - nums[i])
        
        return ans