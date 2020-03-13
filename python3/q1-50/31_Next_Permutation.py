class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        # reverse
        i += 1
        k = len(nums) - 1
        while i < k:
            nums[i], nums[k] = nums[k], nums[i]
            i += 1
            k -= 1
        return


if __name__ == "__main__":
    nums = [2, 1, 3]
    sol = Solution()
    sol.nextPermutation(nums)
    print(nums)


# class Solution:
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """

#         if sorted(nums, reverse=True) == nums:
#             nums.sort()
#             return

#         for r in range(len(nums)-1, -1, -1):
#             for i in range(len(nums)-1, r-1, -1):
#                 for j in range(i-1, r-1, -1):
#                     #                 that would make the second larger number
#                     if nums[i] > nums[j]:
#                         temp = nums[i]
#                         nums[i] = nums[j]
#                         nums[j] = temp
#                         nums[j+1:] = sorted(nums[j+1:])
#                         return
#         nums.sort()
#         return
