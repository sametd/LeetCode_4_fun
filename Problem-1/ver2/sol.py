class Solution(object):
    def twoSum(self, nums, target):
        N = len(nums)
        for i in range(N):
            val1 = nums.pop(0)
            for j, val2 in enumerate(nums):
                if val1 + val2 == target:
                    return (i, i + j + 1)


sol = Solution()
print(sol.twoSum([3, 3], 6))
# Runtime 1780 ms
# Memory 14.2 MB
