# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        dep, level = 0, [root]

        while root and level:
            dep += 1
            for _ in range(len(level)):
                node = level.pop(0)
                if not node.left and not node.right:
                    return dep

                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

        return dep
