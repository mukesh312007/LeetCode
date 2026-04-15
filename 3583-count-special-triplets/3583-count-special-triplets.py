class Solution(object):
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        
        from collections import Counter
        right_count = Counter(nums)
        left_count = Counter()
        
        result = 0
        
        for num in nums:
            right_count[num] -= 1  
            
            target = 2 * num
            result += left_count[target] * right_count[target]
            result %= MOD
            
            left_count[num] += 1  # add to left
        
        return result