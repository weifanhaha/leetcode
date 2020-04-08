from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return None

        def node(val, left, right):
            n = TreeNode(val)
            n.left = left
            n.right = right
            return n

        def generate(start, end):
            return [
                node(i, l, r) for i in range(start, end)
                for l in generate(start, i)
                for r in generate(i+1, end)
            ] or [None]
        return generate(1, n+1)
    # def generateTrees(self, n: int) -> List[TreeNode]:
    #     if n == 0:
    #         return None

    #     def dfs(start, end):
    #         if start > end:
    #             return
    #         ret = []
    #         for i in range(start, end):
    #             for l in self.dfs(start, i) or [None]:
    #                 for r in self.dfs(i+1, end) or [None]:
    #                     node = TreeNode(i)
    #                     node.left, node.right = l, r
    #                     ret.append(node)
    #         return ret

    #     return dfs(1, n+1)


if __name__ == '__main__':
    sol = Solution()
    sol.generateTrees(n)
