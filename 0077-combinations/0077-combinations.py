class Solution(object):
    def combine(self, n, k):
        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return res