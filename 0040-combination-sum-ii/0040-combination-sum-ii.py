class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return res