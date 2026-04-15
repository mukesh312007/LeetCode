class Solution(object):
    def maxSumDivThree(self, nums):
        total = sum(nums)
        
        rem1 = []
        rem2 = []
        
        for num in nums:
            if num % 3 == 1:
                rem1.append(num)
            elif num % 3 == 2:
                rem2.append(num)
        
        rem1.sort()
        rem2.sort()
        
        if total % 3 == 0:
            return total
        
        elif total % 3 == 1:
            option1 = rem1[0] if len(rem1) >= 1 else float('inf')
            option2 = rem2[0] + rem2[1] if len(rem2) >= 2 else float('inf')
            return total - min(option1, option2)
        
        else: 
            option1 = rem2[0] if len(rem2) >= 1 else float('inf')
            option2 = rem1[0] + rem1[1] if len(rem1) >= 2 else float('inf')
            return total - min(option1, option2)