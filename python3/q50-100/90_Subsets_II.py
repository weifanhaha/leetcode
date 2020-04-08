from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums.sort()

        def dfs(nums, ret, idx, path):
            ret.add(tuple(path))

            for i in range(idx, len(nums)):
                dfs(nums, ret, i+1, path + [nums[i]])

        for i in nums:
            dfs(nums, ret, 0, [])

        return [list(path) for path in ret]


if __name__ == '__main__':
    nums = []
    sol = Solution()
    print(sol.subsetsWithDup(nums))
