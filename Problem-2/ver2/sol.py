class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(d):
    hd = ListNode(d[0])
    cr = hd
    for i in d[1:]:
        cr.next = ListNode(i)
        cr = cr.next
    return hd


def print_linked_list(ln):
    while ln:
        print(ln.val)
        ln = ln.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a = []
        b = []
        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next
        N = len(a)
        M = len(b)
        val1 = 0
        val2 = 0
        for i in range(N):
            val1 += a[N - 1 - i] * 10 ** (N - i - 1)
        for i in range(M):
            val2 += b[M - 1 - i] * 10 ** (M - i - 1)
        val3 = int(val1) + int(val2)
        val3_str = str(val3)[::-1]
        res = []
        for l in val3_str:
            res.append(int(l))
        return list_to_linked_list(res)


vals1 = [2, 4, 3]
vals2 = [5, 6, 4]

l1 = list_to_linked_list(vals1)
l2 = list_to_linked_list(vals2)

s = Solution().addTwoNumbers(l1, l2)
print_linked_list(s)
# Runtime 53 ms
# Memory 13.3 MB
