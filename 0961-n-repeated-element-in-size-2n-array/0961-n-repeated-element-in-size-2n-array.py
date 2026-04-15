class Solution(object):
    def repeatedNTimes(self, nums):
        n = len(nums)
        
        for gap in range(1, 4):
            for i in range(n - gap):
                if nums[i] == nums[i + gap]:
                    return nums[i]