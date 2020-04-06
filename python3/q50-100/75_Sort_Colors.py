from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Constant Space
        i, j = 0, 0

        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1

# def sortColors(self, nums: List[int]) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """

#     # Counting Sort
#     counts = [0] * 3
#     for i in nums:
#         counts[i] += 1

#     p = 0
#     for i, c in enumerate(counts):
#         while c > 0:
#             nums[p] = i
#             p += 1
#             c -= 1


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0, 1]
    sol = Solution()
    sol.sortColors(nums)
    print(nums)
