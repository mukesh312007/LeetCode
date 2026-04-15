class Solution(object):
    def maxProfit(self, n, present, future, hierarchy, budget):
        from collections import defaultdict
        
        tree = defaultdict(list)
        for u, v in hierarchy:
            tree[u-1].append(v-1)
        
        def dfs(u):
            dp0 = [0] * (budget + 1)
            dp1 = [0] * (budget + 1)
            
            children_dp = [dfs(v) for v in tree[u]]
            
            temp0 = [0] * (budget + 1)
            temp0[0] = 0
            
            for c0, c1 in children_dp:
                new = [0] * (budget + 1)
                for b in range(budget + 1):
                    for x in range(b + 1):
                        new[b] = max(new[b], temp0[b-x] + c0[x])
                temp0 = new
            
            full_cost = present[u]
            disc_cost = present[u] // 2
            
            full_profit = future[u] - full_cost
            disc_profit = future[u] - disc_cost
            
            temp1_full = [0] * (budget + 1)
            for c0, c1 in children_dp:
                new = [0] * (budget + 1)
                for b in range(budget + 1):
                    for x in range(b + 1):
                        new[b] = max(new[b], temp1_full[b-x] + c1[x])
                temp1_full = new
            
            temp1_disc = temp1_full[:]  
            for b in range(budget + 1):
                dp0[b] = temp0[b]
                dp1[b] = temp0[b]
            
            for b in range(budget, -1, -1):
                if b >= full_cost:
                    dp0[b] = max(dp0[b], temp1_full[b-full_cost] + full_profit)
                
                if b >= disc_cost:
                    dp1[b] = max(dp1[b], temp1_disc[b-disc_cost] + disc_profit)
            
            return dp0, dp1
        
        dp0, _ = dfs(0)
        return max(dp0)