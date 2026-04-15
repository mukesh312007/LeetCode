class Solution(object):
    def sumFourDivisors(self, nums):
        def get_div_sum(x):
            count = 0
            total = 0
            
            i = 1
            while i * i <= x:
                if x % i == 0:
                    j = x // i
                    
                    if i == j:
                        count += 1
                        total += i
                    else:
                        count += 2
                        total += i + j
                    
                    if count > 4:
                        return 0
                i += 1
            
            return total if count == 4 else 0
        
        return sum(get_div_sum(x) for x in nums)