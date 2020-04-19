class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def traverse(node, ret):
            if not node:
                return
            traverse(node.left, ret)
            traverse(node.right, ret)
            ret.append(node.val)

        ret = []
        traverse(root, ret)
        return ret
