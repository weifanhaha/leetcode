class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = nxt.next.next
            curr.next.next = nxt
            curr = curr.next.next
        return dummy.next
