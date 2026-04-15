import heapq

class Solution(object):
    def minCost(self, grid, k):
        m, n = len(grid), len(grid[0])

        # sort all cells by value
        cells = sorted((grid[i][j], i, j) for i in range(m) for j in range(n))

        INF = float('inf')
        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]

        pq = [(0, 0, 0, 0)]
        dist[0][0][0] = 0

        dirs = [(1, 0), (0, 1)]

        while pq:
            cost, x, y, t = heapq.heappop(pq)

            if (x, y) == (m - 1, n - 1):
                return cost

            if cost != dist[x][y][t]:
                continue

            # normal moves
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < m and ny < n:
                    nc = cost + grid[nx][ny]
                    if nc < dist[nx][ny][t]:
                        dist[nx][ny][t] = nc
                        heapq.heappush(pq, (nc, nx, ny, t))

            # teleport: ONLY expand valid targets lazily
            if t < k:
                base = grid[x][y]

                # IMPORTANT FIX:
                # we DO NOT use global pointers
                # we scan only when popped state demands it
                for val, i, j in cells:
                    if val > base:
                        break
                    if cost < dist[i][j][t + 1]:
                        dist[i][j][t + 1] = cost
                        heapq.heappush(pq, (cost, i, j, t + 1))

        return min(dist[m-1][n-1])