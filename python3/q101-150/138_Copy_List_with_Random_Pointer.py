# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        node = head

        while node:
            dic[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            if node.next:
                dic[node].next = dic[node.next]
            if node.random:
                dic[node].random = dic[node.random]
            node = node.next

        return dic[head]
