def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + (max(self.maxDepth(root.right), self.maxDepth(root.left))) if root else 0
    # def maxDepth(self, root: TreeNode) -> int:
    #     dep = 0
    #     level = [root]
    #     while root and level:
    #         for i in range(len(level)):
    #             node = level.pop(0)
    #             if node.left:
    #                 level.append(node.left)
    #             if node.right:
    #                 level.append(node.right)
    #         dep += 1
    #     return dep


if __name__ == "__main__":
    root = deserialize('1, 2, 3')

    sol = Solution()
    print(sol.maxDepth(root))
