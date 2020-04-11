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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def searchPath(node, remain, path, ret):
            if not node:
                return
            if not node.left and not node.right and node.val == remain:
                ret.append(path + [node.val])

            else:
                remain -= node.val

                if node.left:
                    searchPath(node.left, remain, path + [node.val], ret)
                if node.right:
                    searchPath(node.right, remain, path + [node.val], ret)
            return ret

        return searchPath(root, sum, [], [])


if __name__ == "__main__":
    root = deserialize('[-2,null,-3]')
    # root = deserialize('[5,4,8,11,null,13,4,7,2,null,null,5,1]')
    s = -5

    sol = Solution()
    print(sol.pathSum(root, s))
