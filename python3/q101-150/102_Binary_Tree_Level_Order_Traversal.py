from typing import List


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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # same idea, tinier
        ret, level = [], [root]
        while level:
            ret.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left, node.right)
                     if kid]

        return ret

    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if not root:
    #         return []
    #     # BFS
    #     stack = [(root, 0)]
    #     ret = []

    #     while stack:
    #         node, layer = stack.pop(0)
    #         if not ret or layer == len(ret):
    #             ret.append([node.val])
    #         elif layer < len(ret):
    #             ret[-1].append(node.val)

    #         if node.left:
    #             stack.append((node.left, layer+1))
    #         if node.right:
    #             stack.append((node.right, layer+1))
    #         print(stack)
    #         print(ret)

    #     return ret


if __name__ == "__main__":
    root = deserialize('[]')

    sol = Solution()
    print(sol.levelOrder(root))
