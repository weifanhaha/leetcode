# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         l = []
#         for list_node in lists:
#             next_one = list_node
#             while next_one:
#                 l.append(next_one)
#                 next_one = next_one.next
#         sorted_list = sorted(l, key=lambda x: x.val)

#         for i, node in enumerate(sorted_list):
#             try:
#                 node.next = sorted_list[i+1]

#             except:
#                 node.next = None
#                 break

#         if sorted_list:
#             return sorted_list[0]
#         else:
#             return None


class Solution(object):
    def mergeKLists(self, lists):
        l = []
        for list_node in lists:
            node = list_node
            while node:
                l.append(node)
                node = node.next

        if not l:
            return None

        l.sort(key=lambda x: x.val)

        for i, node in enumerate(l):
            if i == len(l)-1:
                node.next = None
            else:
                node.next = l[i+1]

        return l[0]
