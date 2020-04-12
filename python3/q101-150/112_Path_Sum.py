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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        if root.val == sum and not root.left and not root.right:
            return True

        remain = sum - root.val
        return self.hasPathSum(root.left, remain) or self.hasPathSum(root.right, remain)

    # can not handle case [], 0
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #     if not root:
    #         return True if not sum else False

    #     remain = sum - root.val
    #     return self.hasPathSum(root.left, remain) or self.hasPathSum(root.right, remain)


if __name__ == "__main__":
    root = deserialize('[1,2,3]')
    s = 2

    sol = Solution()
    print(sol.hasPathSum(root, s))
