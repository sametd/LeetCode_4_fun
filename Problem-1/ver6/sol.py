class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, val in enumerate(nums):
            if val in seen:
                return [seen[val], i]
            seen[target - val] = i


sol = Solution()
print(sol.twoSum([3, 3], 6))
# Runtime 37 ms
# Memory 14 MB
