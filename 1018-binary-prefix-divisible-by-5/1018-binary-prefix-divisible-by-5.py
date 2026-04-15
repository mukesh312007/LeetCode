class Solution(object):
    def prefixesDivBy5(self, nums):
        result = []
        rem = 0
        
        for bit in nums:
            rem = (rem * 2 + bit) % 5
            result.append(rem == 0)
        
        return result