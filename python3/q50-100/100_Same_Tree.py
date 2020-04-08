# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # True only when p == q == None
        return p is q

    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # if not p and not q:
        #     return True
        # if (p and not q) or (q and not p) or (p.val != q.val):
        #     return False

        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    p = deserialize('[1,2]')
    q = deserialize('[1]')
    sol = Solution()
    print(sol.isSameTree(p, q))
