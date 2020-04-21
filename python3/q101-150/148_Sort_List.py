class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def mergeList(h1, h2):
            dummy = new_head = ListNode(0)
            while h1 and h2:
                if h1.val <= h2.val:
                    new_head.next = h1
                    h1 = h1.next
                else:
                    new_head.next = h2
                    h2 = h2.next
                new_head = new_head.next

            new_head.next = h1 or h2
            return dummy.next

        # find the middle of the list
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        # sort and merge list
        return mergeList(self.sortList(head), self.sortList(slow))
