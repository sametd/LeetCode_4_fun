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
        multiplier = 1
        val1 = 0
        val2 = 0
        while l1:
            val1 += multiplier * l1.val
            multiplier *= 10
            l1 = l1.next
        multiplier = 1
        while l2:
            val2 += multiplier * l2.val
            multiplier *= 10
            l2 = l2.next

        val3 = val1 + val2
        val3_str = str(val3)
        res = []
        for l in val3_str:
            res.append(int(l))
        res.reverse()
        return list_to_linked_list(res)


vals1 = [2, 4, 3]
vals2 = [5, 6, 4]

l1 = list_to_linked_list(vals1)
l2 = list_to_linked_list(vals2)

s = Solution().addTwoNumbers(l1, l2)
print_linked_list(s)
# Runtime 33 ms
# Memory 13.5 MB
