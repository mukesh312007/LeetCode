class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**18
        
        dist = [[INF] * 26 for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0
        
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - 97
            v = ord(c) - 97
            dist[u][v] = min(dist[u][v], w)
        
        for k in range(26):
            for i in range(26):
                if dist[i][k] == INF:
                    continue
                for j in range(26):
                    if dist[k][j] == INF:
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        ans = 0
        for a, b in zip(source, target):
            if a == b:
                continue
            u = ord(a) - 97
            v = ord(b) - 97
            if dist[u][v] == INF:
                return -1
            ans += dist[u][v]
        
        return ans