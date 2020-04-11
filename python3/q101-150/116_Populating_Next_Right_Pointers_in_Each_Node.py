"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        level = [root, None]
        while root and level:
            node = level.pop(0)
            if node:
                node.next = level[0]
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            else:
                # end of level
                if len(level) > 0:
                    level.append(None)

