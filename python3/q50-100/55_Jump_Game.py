from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        _max = 0
        for i, n in enumerate(nums):
            if i > _max:
                return False
            _max = max(_max, i + n)

        return True


if __name__ == "__main__":
    # nums = [2, 3, 1, 1, 4]
    # nums = [2, 0, 5]
    nums = [3, 2, 1, 0, 4]
    sol = Solution()
    print(sol.canJump(nums))
