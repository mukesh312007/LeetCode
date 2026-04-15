class Solution(object):
    def countPermutations(self, complexity):
        MOD = 10**9 + 7
        n = len(complexity)
        
        min_so_far = complexity[0]
        
        for i in range(1, n):
            if complexity[i] <= min_so_far:
                return 0
            min_so_far = min(min_so_far, complexity[i])
        
        result = 1
        choices = 1  
        
        for i in range(1, n):
            result = (result * choices) % MOD
            choices += 1
        
        return result