class Solution(object):
    def getDescentPeriods(self, prices):
        result = 0
        length = 1  # current descent streak
        
        for i in range(len(prices)):
            if i > 0 and prices[i] == prices[i-1] - 1:
                length += 1
            else:
                length = 1
            
            result += length
        
        return result