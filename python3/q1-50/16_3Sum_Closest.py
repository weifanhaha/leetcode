from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) <= 3:
            return sum(nums)
        nums.sort()
        closest = 999999
        i = 0

        while i < len(nums) - 2:
            while 0 < i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1

            l = i + 1
            r = len(nums) - 1
            while l < r:
                nsum = nums[i] + nums[l] + nums[r]
                if abs(nsum-target) < abs(closest-target):
                    closest = nsum

                if nsum > target:
                    r -= 1
                elif nsum < target:
                    l += 1

                else:
                    return nsum
            i += 1

        return closest


if __name__ == "__main__":
    # nums = [-4, -1, 1, 2]
    nums = [1, 1, 1, 1]
    target = 100
    sol = Solution()
    ans = sol.threeSumClosest(nums, target)
    print(ans)
