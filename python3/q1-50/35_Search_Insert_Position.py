class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # for i, num in enumerate(nums):
        #     if target <= num:
        #         return i
        # return len(nums)

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l


if __name__ == "__main__":
    nums = []
    target = 7

    sol = Solution()
    print(sol.searchInsert(nums, target))
