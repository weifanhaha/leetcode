# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        node = head
        leng = 0
        while node:
            node = node.next
            leng += 1

        k %= leng
        tail = node = head

        for _ in range(k):
            tail = tail.next

        while tail.next:
            tail = tail.next
            node = node.next

        tail.next = dummy.next
        dummy.next = node.next
        node.next = None
        return dummy.next

    def print_node(self, head: ListNode):
        ret = []
        node = head
        while node:
            ret.append(node.val)
            node = node.next
        print(ret)


if __name__ == "__main__":
    head = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(4)
    n4 = ListNode(5)

    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    k = 5

    sol = Solution()
    head = sol.rotateRight(head, k)
    sol.print_node(head)
