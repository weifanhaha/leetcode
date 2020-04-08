
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode, floor=float('-inf'), ceiling=float('inf')) -> bool:
        if not root:
            return True

        if root.val <= floor or root.val >= ceiling:
            return False

        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)
