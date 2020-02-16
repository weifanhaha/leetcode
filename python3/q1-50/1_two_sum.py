from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(nums):
            if num not in dic:
                dic[target-num] = idx
            else:
                return [dic[num], idx]


if __name__ == "__main__":

    nums = [3, 2, 4]
    target = 6

    sol = Solution()
    ans = sol.twoSum(nums, target)
    print(ans)
