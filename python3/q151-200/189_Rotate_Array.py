from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(l, i, j):
            while i < j:
                l[i], l[j] = l[j], l[i]
                i, j = i + 1, j - 1

        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums) - 1)

    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """

    #     k = k % len(nums)
    #     for _ in range(k):
    #         nums.insert(0, nums.pop())


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    sol = Solution()
    sol.rotate(nums, k)
    print(nums)
