class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        a, b = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        N, M = len(a), len(b)  # M >= 1

        total_len = N + M
        num_to_take = (total_len + 1) // 2

        is_even = total_len % 2 == 0

        i = 0
        j = 0
        k = 0
        if N == 0:
            a.append(10**6)
        if M == 0:
            b.append(10**6)
        while i < num_to_take:
            if j == N:
                curr = b[k]
                k += 1
                i += 1
                continue
            if k == M:
                curr = a[j]
                j += 1
                i += 1
                continue
            if a[j] < b[k]:
                curr = a[j]
                j += 1
            else:
                curr = b[k]
                k += 1
            i += 1

        if is_even:
            if j < N:
                next = a[j] if a[j] >= curr else b[k]
            else:
                next = b[k]
            if k < M:
                if b[k] < next:
                    next = b[k]
            return (next + curr) / 2.0
        else:
            return curr

a = [4]
b = [1, 2, 3]

s = Solution()
print(s.findMedianSortedArrays(a, b))
# Runtime 53 ms
# Memory 13.5 MB