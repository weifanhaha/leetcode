# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, dummy.next

        while curr:
            if curr.next and curr.val == curr.next.val:
                curr_val = curr.val
                while curr and curr.val == curr_val:
                    curr = curr.next
                prev.next = curr
            else:
                prev, curr = curr, curr.next

        return dummy.next

    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return

    #     dummy = pre = ListNode(0)
    #     dummy.next = head

    #     node = head
    #     while node and node.next:
    #         if node.val == node.next.val:
    #             while node and node.next and node.val == node.next.val:
    #                 node = node.next
    #             node = node.next
    #             pre.next = node
    #         else:
    #             pre = pre.next
    #             node = node.next

    #     return dummy.next

    def print_node(self, head: ListNode):
        ret = []
        node = head
        while node:
            ret.append(node.val)
            node = node.next
        print(ret)


if __name__ == "__main__":

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(3)
    n5 = ListNode(4)
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
