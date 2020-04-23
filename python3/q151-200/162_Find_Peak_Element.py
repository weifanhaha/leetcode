from typing import List


class Solution:
    # O(lg(N))
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[m] < nums[m+1]:
                l = m + 1
            else:
                r = m
        return l

    # O(N)
    # def findPeakElement(self, nums: List[int]) -> int:
    #     nums = [float('-inf')] + nums + [float('-inf')]
    #     for i in range(1, len(nums) - 1):
    #         if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
    #             return i - 1


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 5, 6, 4]
    sol = Solution()
    print(sol.findPeakElement(nums))
