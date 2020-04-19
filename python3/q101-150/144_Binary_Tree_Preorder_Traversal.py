from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret

    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     def traverse(node, ret):
    #         if not node:
    #             return
    #         ret.append(node.val)
    #         traverse(node.left, ret)
    #         traverse(node.right, ret)

    #     ret = []
    #     traverse(root, ret)
    #     return ret
