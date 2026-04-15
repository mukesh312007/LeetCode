class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        from collections import defaultdict
        INF = 10**18

        # collect all nodes (strings)
        nodes = set(original + changed)
        nodes = list(nodes)
        idx = {s:i for i,s in enumerate(nodes)}
        m = len(nodes)

        # distance graph
        dist = [[INF]*m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        # edges
        for o, c, w in zip(original, changed, cost):
            u, v = idx[o], idx[c]
            dist[u][v] = min(dist[u][v], w)

        # Floyd-Warshall
        for k in range(m):
            for i in range(m):
                if dist[i][k] == INF:
                    continue
                for j in range(m):
                    if dist[k][j] == INF:
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        n = len(source)

        # dp[i] = min cost from i to end
        dp = [INF]*(n+1)
        dp[n] = 0

        # try match substrings
        for i in range(n-1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i+1]

            # try all strings starting at i
            for s in nodes:
                ls = len(s)
                if i + ls > n:
                    continue
                if source[i:i+ls] != s:
                    continue

                for t in nodes:
                    if target[i:i+ls] != t:
                        continue
                    if dist[idx[s]][idx[t]] == INF:
                        continue
                    dp[i] = min(dp[i], dist[idx[s]][idx[t]] + dp[i+ls])

        return -1 if dp[0] >= INF else dp[0]