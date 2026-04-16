from collections import defaultdict

class Solution(object):
    def solveQueries(self, nums, queries):
        n = len(nums)
        pos = defaultdict(list)

        # 1. store indices for each value
        for i, v in enumerate(nums):
            pos[v].append(i)

        # distance array
        best = [-1] * n

        # 2. process each value group
        for arr in pos.values():
            m = len(arr)

            if m == 1:
                continue

            for i in range(m):
                cur = arr[i]
                prev = arr[i - 1]
                nxt = arr[(i + 1) % m]

                # circular distance
                d1 = abs(cur - prev)
                d1 = min(d1, n - d1)

                d2 = abs(cur - nxt)
                d2 = min(d2, n - d2)

                best[cur] = min(d1, d2)

        # 3. answer queries
        return [best[i] for i in queries]