# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_height(node):
            if node is None:
                return 0

            left = check(root.left)
            right = check(root.right)

            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return 1 + max(left, right)

        return check_height(root) != -1