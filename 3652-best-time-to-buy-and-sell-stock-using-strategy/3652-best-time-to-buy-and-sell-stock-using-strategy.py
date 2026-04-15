class Solution(object):
    def maxProfit(self, prices, strategy, k):
        n = len(prices)
        
        # base profit
        base = sum(strategy[i] * prices[i] for i in range(n))
        
        half = k // 2
        
        # precompute contributions
        A = [-strategy[i] * prices[i] for i in range(n)]              # first half
        B = [prices[i] - strategy[i] * prices[i] for i in range(n)]   # second half
        
        # prefix sums
        preA = [0] * (n + 1)
        preB = [0] * (n + 1)
        
        for i in range(n):
            preA[i+1] = preA[i] + A[i]
            preB[i+1] = preB[i] + B[i]
        
        max_gain = 0
        
        for l in range(n - k + 1):
            mid = l + half
            r = l + k
            
            gain = (preA[mid] - preA[l]) + (preB[r] - preB[mid])
            max_gain = max(max_gain, gain)
        
        return base + max_gain