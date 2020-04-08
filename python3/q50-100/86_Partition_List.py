# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)

        h1.next = l1
        h2.next = l2

        while head:
            if head.val >= x:
                l2.next = head
                l2 = l2.next
            else:
                l1.next = head
                l1 = l1.next
            head = head.next

        l2.next = None
        l1.next = h2.next

        return h1.next

    def print_node(self, head: ListNode):
        ret = []
        node = head
        while node:
            ret.append(node.val)
            node = node.next
        print(ret)


if __name__ == "__main__":

    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n4 = ListNode(2)
    n5 = ListNode(5)
    n6 = ListNode(2)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    x = 3
    sol = Solution()
    head = sol.partition(n1, x)

    sol.print_node(head)
