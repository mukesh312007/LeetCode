class Solution(object):
    def minBitwiseArray(self, nums):
        res = []
        
        for num in nums:
            if num % 2 == 0:
                res.append(-1)
                continue
            
            x = num
            bit = 1
            
            while num & bit:
                bit <<= 1
            
            x = num ^ (bit >> 1)
            res.append(x)
        
        return res