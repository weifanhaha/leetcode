# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
        except AttributeError:
            return None

        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next
        return head

    # def detectCycle(self, head: ListNode) -> ListNode:
    #     traversed = set()

    #     while head:
    #         if head in traversed:
    #             return head

    #         traversed.add(head)
    #         head = head.next
    #     return None
