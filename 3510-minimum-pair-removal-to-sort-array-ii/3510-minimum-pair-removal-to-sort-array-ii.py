import heapq

class Solution(object):
    def minimumPairRemoval(self, nums):
        n = len(nums)
        
        prev = list(range(-1, n-1))
        next = list(range(1, n+1))
        next[-1] = -1
        
        alive = [True] * n
        
        # count violations
        bad = 0
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                bad += 1
        
        # min heap of (sum, index)
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i+1], i))
        
        operations = 0
        
        while bad > 0:
            # get valid pair
            while True:
                s, i = heapq.heappop(heap)
                j = next[i]
                if j != -1 and alive[i] and alive[j] and nums[i] + nums[j] == s:
                    break
            
            j = next[i]
            
            # remove old violations
            if prev[i] != -1 and nums[prev[i]] > nums[i]:
                bad -= 1
            if nums[i] > nums[j]:
                bad -= 1
            if next[j] != -1 and nums[j] > nums[next[j]]:
                bad -= 1
            
            # merge
            nums[i] += nums[j]
            alive[j] = False
            
            nj = next[j]
            next[i] = nj
            if nj != -1:
                prev[nj] = i
            
            # add new violations
            if prev[i] != -1 and nums[prev[i]] > nums[i]:
                bad += 1
            if next[i] != -1 and nums[i] > nums[next[i]]:
                bad += 1
            
            # push new pairs
            if prev[i] != -1:
                p = prev[i]
                heapq.heappush(heap, (nums[p] + nums[i], p))
            if next[i] != -1:
                heapq.heappush(heap, (nums[i] + nums[next[i]], i))
            
            operations += 1
        
        return operations