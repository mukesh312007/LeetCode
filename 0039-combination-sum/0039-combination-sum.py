class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])  # i allows reuse
                path.pop()

        backtrack(0, [], target)
        return res