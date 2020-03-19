from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)

        # ignore the nums larger than the size or less than 0
        # because it won't be the first missing positive

        for i in range(n):
            if nums[i] >= n or nums[i] < 0:
                nums[i] = 0

        # use the index to check which is missing
        for i in range(n):
            nums[nums[i] % n] += n

        for i in range(1, n):
            if nums[i] // n == 0:
                return i

        return n


if __name__ == "__main__":
    nums = [2, 2]
    sol = Solution()
    print(sol.firstMissingPositive(nums))
