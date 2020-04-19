import collections


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        queue = collections.deque([node])
        node_copy = Node(node.val)
        dic = {node: node_copy}

        while queue:
            v = queue.popleft()

            for n in v.neighbors:
                # not traversed yet
                if n not in dic:
                    new_n = Node(n.val)
                    dic[n] = new_n
                    dic[v].neighbors.append(new_n)
                    queue.append(n)
                else:
                    dic[v].neighbors.append(dic[n])

        return node_copy
