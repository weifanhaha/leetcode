class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if mid == r and nums[mid] != target and nums[l] != target:
                return [-1, -1]

            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                lo = hi = mid
                while (lo >= 0 and nums[lo] == target):
                    lo -= 1
                while (hi < len(nums) and nums[hi] == target):
                    hi += 1
                return [lo+1, hi-1]

        return [-1, -1]


# class Solution:
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         if len(nums) == 0:
#             return [-1, -1]
#         return self.search_with_index(nums, target, 0, len(nums)-1)

#     def search_with_index(self, nums, target, i, j):
#         mid = (i+j) // 2

#         if mid == i and nums[mid] != target and nums[j] != target:
#             return [-1, -1]

#         if nums[mid] > target:
#             return self.search_with_index(nums, target, i, mid)
#         elif nums[mid] < target:
#             return self.search_with_index(nums, target, mid+1, j)
#         else:
#             l = r = mid
#             while (l >= 0 and nums[l] == target):
#                 l -= 1
#             while (r < len(nums) and nums[r] == target):
#                 r += 1
#             return [l+1, r-1]


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 11

    sol = Solution()
    print(sol.searchRange(nums, target))
