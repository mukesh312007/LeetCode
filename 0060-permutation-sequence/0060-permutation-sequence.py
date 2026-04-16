class Solution(object):
    def getPermutation(self, n, k):
        from math import factorial

        nums = [str(i) for i in range(1, n + 1)]
        k -= 1  
        result = []

        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            index = k // fact

            result.append(nums[index])
            nums.pop(index)

            k %= fact

        return "".join(result)