from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid if nums[r] != nums[mid] else r - 1

        return nums[l]


if __name__ == '__main__':
    nums = [1, 1, 2, 3, 5, 5, 5, 5]
    sol = Solution()
    print(sol.findMin(nums))
