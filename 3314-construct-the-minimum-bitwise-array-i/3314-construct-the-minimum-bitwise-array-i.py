class Solution(object):
    def minBitwiseArray(self, nums):
        res = []
        
        for num in nums:
            if num % 2 == 0:
                res.append(-1)
                continue
            
            temp = num
            count = 0
            while temp & 1:
                count += 1
                temp >>= 1
            
            x = num ^ (1 << (count - 1))
            res.append(x)
        
        return res