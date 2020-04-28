# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.recursive_sum(root.left, True) + self.recursive_sum(root.right, False)

    def recursive_sum(self, node, is_left):
        if not node:
            return 0
        if (not node.left and not node.right):
            return node.val if is_left else 0

        return self.recursive_sum(node.left, True) + self.recursive_sum(node.right, False)


if __name__ == '__main__':
    # build tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    sol = Solution()
    print(sol.sumOfLeftLeaves(root))
    # should be 24
