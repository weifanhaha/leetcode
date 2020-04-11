from typing import List

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def sortedArr2BST(nums, l, r):
            if l == r:
                return
            mid = (l+r) // 2
            root = TreeNode(nums[mid])
            root.left = sortedArr2BST(nums, l, mid)
            root.right = sortedArr2BST(nums, mid+1, r)
            return root

        return sortedArr2BST(nums, 0, len(nums) - 1)

    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    #     if not nums:
    #         return
    #     mid = len(nums) // 2
    #     root = TreeNode(nums[mid])
    #     root.left = self.sortedArrayToBST(nums[:mid])
    #     root.right = self.sortedArrayToBST(nums[mid+1:])
    #     return root
