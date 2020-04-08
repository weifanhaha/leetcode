# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head

        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next

            curr = curr.next

        return head

    def print_node(self, head: ListNode):
        ret = []
        node = head
        while node:
            ret.append(node.val)
            node = node.next
        print(ret)


if __name__ == "__main__":

    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(3)
    n4 = ListNode(3)
    n5 = ListNode(3)
    n6 = ListNode(4)
    n7 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    sol = Solution()
    head = sol.deleteDuplicates(n1)

    sol.print_node(head)
