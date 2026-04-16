class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)

        closest = float('inf')

        for i in range(n - 2):
            l, r = i + 1, n - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                # update closest
                if abs(total - target) < abs(closest - target):
                    closest = total

                if total == target:
                    return total
                elif total < target:
                    l += 1
                else:
                    r -= 1

        return closest