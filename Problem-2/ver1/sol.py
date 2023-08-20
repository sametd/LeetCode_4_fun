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
        hd = ListNode()
        cr = hd
        rm = 0

        while (l1 != None) or (l2 != None) or rm:
            cr.val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + rm
            rm = 0
            if cr.val > 9:
                cr.val -= 10
                rm = 1
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 == None and l2 == None and rm == 0:
                break
            cr.next = ListNode()
            cr = cr.next
        return hd


vals1 = [2, 4, 3]
vals2 = [5, 6, 4]

l1 = list_to_linked_list(vals1)
l2 = list_to_linked_list(vals2)

s = Solution().addTwoNumbers(l1, l2)
print_linked_list(s)
# Runtime 47 ms
# Memory 13.3 MB
