class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        lo = 0
        hi = len(nums)

        while (lo < hi):
            mid = (lo + hi) // 2
            if (nums[mid] < nums[0]) == (target < nums[0]):
                num = nums[mid]
            else:
                num = -999999 if target < nums[0] else 99999

            if (num < target):
                lo = mid + 1
            elif (num > target):
                hi = mid
            else:
                return mid

        return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3

    sol = Solution()
    ans = sol.search(nums, target)
    print(ans)
