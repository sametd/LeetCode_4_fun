class Solution(object):
    def twoSum(self, nums, target):
        for i, val1 in enumerate(nums):
            for j, val2 in enumerate(nums[i + 1 :]):
                if val1 + val2 == target:
                    return [i, i + 1 + j]


sol = Solution()
print(sol.twoSum([3, 3], 6))
# Runtime 1827 ms
# Memory 14.1 MB
