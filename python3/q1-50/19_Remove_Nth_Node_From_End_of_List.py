# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        for i in range(n):
            first = first.next

        while first.next:
            first = first.next
            second = second.next

        # when first reach the tail, second.next is the nth from tail
        # remove second.next
        second.next = second.next.next

        return dummy.next

    @staticmethod
    def print_list_node(head: ListNode):
        pointer = head
        while pointer:
            print(pointer.val)
            pointer = pointer.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    n = 2

    sol = Solution()
    ans = sol.removeNthFromEnd(l1, 2)

    Solution.print_list_node(ans)
