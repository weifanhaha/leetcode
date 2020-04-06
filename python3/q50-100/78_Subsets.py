from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def dfs(nums, idx, path, ret):
            ret.append(path)
            for i in range(idx, len(nums)):
                dfs(nums, i+1, path + [nums[i]], ret)

        dfs(nums, 0, [], ret)
        return ret


if __name__ == "__main__":
    nums = [1, 3, 2]
    sol = Solution()
    print(sol.subsets(nums))
