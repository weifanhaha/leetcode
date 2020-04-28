class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
            else:
                lo = hi = mid
                while lo > 0 and nums[lo - 1] == target:
                    lo -= 1
                while hi < len(nums) - 1 and nums[hi + 1] == target:
                    hi += 1

                return [lo, hi]
        return [-1, -1]

    # def search(self, nums, target):
    #     l, r = 0, len(nums) - 1
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if nums[mid] == target:
    #             return mid
    #         if nums[l] < nums[mid]:
    #             if nums[l] <= target <= nums[mid]:
    #                 r = mid - 1
    #             else:
    #                 l = mid + 1
    #         else:
    #             if nums[mid] <= target <= nums[r]:
    #                 l = mid + 1
    #             else:
    #                 r = mid - 1

    #     return -1

    # def search(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """

    #     lo = 0
    #     hi = len(nums)

    #     while (lo < hi):
    #         mid = (lo + hi) // 2
    #         if (nums[mid] < nums[0]) == (target < nums[0]):
    #             num = nums[mid]
    #         else:
    #             num = -999999 if target < nums[0] else 99999

    #         if (num < target):
    #             lo = mid + 1
    #         elif (num > target):
    #             hi = mid
    #         else:
    #             return mid

    #     return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 2

    sol = Solution()
    ans = sol.search(nums, target)
    print(ans)
