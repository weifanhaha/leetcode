
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        ref1 = l1
        ref2 = l2
        root = ListNode(0)
        ref = root
        add_one = False

        while ref1 or ref2:
            val = 0
            if ref1:
                val += ref1.val
                ref1 = ref1.next
            if ref2:
                val += ref2.val
                ref2 = ref2.next

            if add_one:
                val += 1
            if val > 9:
                val -= 10
                add_one = True
            else:
                add_one = False
            ref.next = ListNode(val)

            ref = ref.next
        if add_one:
            ref.next = ListNode(1)

        return root.next

        # Need to handle integer overflow
        # ans = 0
        # order = 0

        # ref1 = l1
        # ref2 = l2

        # while ref1 or ref2:
        #     tmp = 0
        #     if ref1:
        #         tmp += ref1.val
        #         ref1 = ref1.next
        #     if ref2:
        #         tmp += ref2.val
        #         ref2 = ref2.next
        #     ans += tmp*(10**order)
        #     order += 1

        # # ans to ListNode
        # if not ans:
        #     return ListNode(0)

        # root = ListNode(0)
        # ref = root
        # while ans:
        #     ref.next = ListNode(ans % 10)
        #     ref = ref.next
        #     ans = int(ans/10)

        # return root.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1_1 = ListNode(0)
    l1_2 = ListNode(0)
    l1_3 = ListNode(0)
    l1_4 = ListNode(0)
    l1_5 = ListNode(0)
    l1_6 = ListNode(0)
    l1_7 = ListNode(0)
    l1_8 = ListNode(0)
    l1_9 = ListNode(0)
    l1_10 = ListNode(0)
    l1_11 = ListNode(0)
    l1_12 = ListNode(0)
    l1_13 = ListNode(0)
    l1_14 = ListNode(0)
    l1_15 = ListNode(0)
    l1_16 = ListNode(0)
    l1_17 = ListNode(0)
    l1_18 = ListNode(0)
    l1_19 = ListNode(0)
    l1_20 = ListNode(0)
    l1_21 = ListNode(0)
    l1_22 = ListNode(1)
    l1.next = l1_1
    l1_1.next = l1_2
    l1_2.next = l1_3
    l1_3.next = l1_4
    l1_4.next = l1_5
    l1_5.next = l1_6
    l1_6.next = l1_7
    l1_7.next = l1_8
    l1_8.next = l1_9
    l1_9.next = l1_10
    l1_10.next = l1_11
    l1_11.next = l1_12
    l1_12.next = l1_13
    l1_13.next = l1_14
    l1_14.next = l1_15
    l1_15.next = l1_16
    l1_16.next = l1_17
    l1_17.next = l1_18
    l1_18.next = l1_19
    l1_19.next = l1_20
    l1_20.next = l1_21
    l1_21.next = l1_22

    l2 = ListNode(5)
    l2_1 = ListNode(6)
    l2_2 = ListNode(4)
    l2.next = l2_1
    l2_1.next = l2_2

    sol = Solution()

    ans = sol.addTwoNumbers(l1, l2)
    # ans = sol.addTwoNumbers(ListNode(0), ListNode(0))

    ref = ans
    while ref:
        print("{}".format(ref.val))
        ref = ref.next
