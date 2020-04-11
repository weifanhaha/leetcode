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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ret, level = [], [root]
        while root and level:
            tmp = []
            for _ in range(len(level)):
                node = level.pop(0)
                tmp.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            ret.insert(0, tmp)
        return ret


if __name__ == '__main__':
    root = deserialize('[3,9,20,null,null,15,7]')

    sol = Solution()
    print(sol.levelOrderBottom(root))
