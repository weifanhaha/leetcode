class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        traversed = set()
        while headA or headB:
            if headA:
                if headA in traversed:
                    return headA
                traversed.add(headA)
                headA = headA.next

            if headB:
                if headB in traversed:
                    return headB
                traversed.add(headB)
                headB = headB.next
        return None
