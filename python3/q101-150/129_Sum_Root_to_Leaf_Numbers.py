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
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack, sumn = [(root, root.val)], 0
        while stack:
            node, path_num = stack.pop()
            if not node.left and not node.right:
                sumn += path_num
            if node.left:
                stack.append((node.left, path_num * 10 + node.left.val))
            if node.right:
                stack.append((node.right, path_num * 10 + node.right.val))

        return sumn


if __name__ == "__main__":
    root = deserialize('[4,9,0,5,1]')
    sol = Solution()
    print(sol.sumNumbers(root))
