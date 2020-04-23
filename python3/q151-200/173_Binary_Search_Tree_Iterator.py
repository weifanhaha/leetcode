class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


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


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.tree = []
        self.parse_tree(root)
        self.ptr = -1

    def parse_tree(self, node):
        if not node:
            return
        self.parse_tree(node.left)
        self.tree.append(node.val)
        self.parse_tree(node.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.ptr += 1
        if self.ptr < len(self.tree):
            return self.tree[self.ptr]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.ptr < len(self.tree) - 1


if __name__ == "__main__":
    root = deserialize('[7,3,15,null,null,9,20]')
    iterator = BSTIterator(root)
    print(iterator.next())
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())
