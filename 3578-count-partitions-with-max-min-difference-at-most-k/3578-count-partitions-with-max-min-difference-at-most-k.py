class Solution(object):
    def countPartitions(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)
        
        from collections import deque
        
        max_d = deque()
        min_d = deque()
        
        dp = [0] * (n + 1)
        dp[0] = 1
        
        prefix = [0] * (n + 2)
        prefix[1] = 1  # prefix[1] = dp[0]
        
        l = 0
        
        for r in range(n):
            # maintain max deque
            while max_d and nums[max_d[-1]] <= nums[r]:
                max_d.pop()
            max_d.append(r)
            
            # maintain min deque
            while min_d and nums[min_d[-1]] >= nums[r]:
                min_d.pop()
            min_d.append(r)
            
            # shrink window if invalid
            while nums[max_d[0]] - nums[min_d[0]] > k:
                if max_d[0] == l:
                    max_d.popleft()
                if min_d[0] == l:
                    min_d.popleft()
                l += 1
            
            # compute dp[r+1]
            dp[r+1] = (prefix[r+1] - prefix[l]) % MOD
            
            # update prefix
            prefix[r+2] = (prefix[r+1] + dp[r+1]) % MOD
        
        return dp[n]