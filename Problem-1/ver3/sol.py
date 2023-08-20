class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i] + nums[j]) == target:
                    return [j, i]


sol = Solution()
print(sol.twoSum([3, 3], 6))
# Runtime 2139 ms
# Memory 14.2 MB
