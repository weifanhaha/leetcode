from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # iterative, with stack
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ret = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                ret.append(node.val)
                root = node.right
        return ret

    # recurcive
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     def traverse(node, ret):
    #         if not node:
    #             return
    #         traverse(node.left, ret)
    #         ret.append(node.val)
    #         traverse(node.right, ret)

    #     ret = []
    #     traverse(root, ret)
    #     return ret


if __name__ == '__main__':

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n1.right = n2
    n2.left = n3

    sol = Solution()
    print(sol.inorderTraversal(n1))
