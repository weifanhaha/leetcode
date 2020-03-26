class Solution:
    def maxSubArray(self, nums):
        cur_max = -2147483648
        tmp = 0
        for n in nums:
            tmp += n
            if tmp > cur_max:
                cur_max = tmp

            if tmp < 0:
                tmp = 0

        return cur_max


if __name__ == "__main__":
    nums = [-2, 1, 3, 9, -11, 8, 3, -2, 5, 6]
    sol = Solution()
    print(sol.maxSubArray(nums))

# Divide and Conquer Solution
# class Solution:
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

#         left, right, max_sum = self.max_sub(nums, 0, len(nums)-1)
#         return max_sum

#     ### divide and conquer
#     def max_sub(self, nums, i, j):
#         if i == j:
#             return i, j, nums[i]
#         else:
#             mid = (i + j) // 2
#             l_low, l_high, l_sum = self.max_sub(nums, i, mid)
#             r_low, r_high, r_sum = self.max_sub(nums, mid + 1, j)
#             c_low, c_high, c_sum = self.max_cross_sub(nums, i, mid, j)

#             if l_sum >= r_sum and l_sum >= c_sum:    # case 1, l_sum is max
#                 return l_low, l_high, l_sum
#             elif r_sum >= l_sum and r_sum >= c_sum:    # case 2, r_sum is max
#                 return r_low, r_high, r_sum
#             else:    # case 3, c_sum is max
#                 return c_low, c_high, c_sum

#     def max_cross_sub(self, nums, i, mid, j):
#         MIN_INT = -10 ^ 6
#         max_left_sum = max_right_sum = MIN_INT
#         left_sum = right_sum = 0
#         max_left = max_right = 0
#         for left in range(mid, i-1, -1):
#             left_sum += nums[left]
#             if left_sum > max_left_sum:
#                 max_left_sum = left_sum
#                 max_left = left

#         for right in range(mid + 1, j+1):
#             right_sum += nums[right]
#             if right_sum > max_right_sum:
#                 max_right_sum = right_sum
#                 max_right = right

#         return max_left, max_right, max_left_sum + max_right_sum
