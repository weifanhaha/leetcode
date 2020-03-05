from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        if len(nums) < 3:
            return ans

        nums.sort()
        i = 0
        while i < len(nums) - 2:
            if nums[i] > 0:
                break
            while 0 < i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1
            j = i + 1
            k = len(nums) - 1
            while j < k:
                nsum = nums[i]+nums[j]+nums[k]
                if(nsum > 0):
                    k -= 1
                elif(nsum < 0):
                    j += 1
                else:
                    pair = [nums[i], nums[j], nums[k]]
                    ans.append(pair)
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
            i += 1
        return ans


if __name__ == "__main__":
    nums = [0, 0, 0, 0, 0, 0]
    # nums = [-1, -1, 0, 1]
    sol = Solution()
    ans = sol.threeSum(nums)
    print(ans)
