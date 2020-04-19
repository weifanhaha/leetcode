# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # find the middle of the list
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next
        p2 = fast.next if fast.next else fast

        # reverse the second half
        prev = slow
        curr = slow.next
        prev.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # zigzag
        p1 = head
        while p2.next:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2
