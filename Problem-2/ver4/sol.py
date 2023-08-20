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
        l1i = 0
        multiplier = 1
        while l1:
            l1i += multiplier * l1.val
            multiplier *= 10
            l1 = l1.next

        l2i = 0
        multiplier = 1
        while l2:
            l2i += multiplier * l2.val
            multiplier *= 10
            l2 = l2.next

        s = str(l1i + l2i)[::-1]

        hd = ListNode(int(s[0]))
        cr = hd
        for i in s[1:]:
            cr.next = ListNode(int(i))
            cr = cr.next

        return hd


vals1 = [2, 4, 3]
vals2 = [5, 6, 4]

l1 = list_to_linked_list(vals1)
l2 = list_to_linked_list(vals2)

s = Solution().addTwoNumbers(l1, l2)
print_linked_list(s)
# Runtime 39 ms
# Memory 13.3 MB
