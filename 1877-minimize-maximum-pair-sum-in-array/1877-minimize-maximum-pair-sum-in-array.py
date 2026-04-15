class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        
        left, right = 0, len(nums) - 1
        max_pair_sum = 0
        
        while left < right:
            max_pair_sum = max(max_pair_sum, nums[left] + nums[right])
            left += 1
            right -= 1
        
        return max_pair_sum