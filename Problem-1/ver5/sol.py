class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(len(nums)):
            t = target - nums[i]
            for j in range(i + 1, n):
                if nums[j] == t:
                    return [i, j]


sol = Solution()
print(sol.twoSum([3, 3], 6))
# Runtime 1428 ms
# Memory 14.2 MB
