from typing import List


class Solution:
    # no extra space with xor
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]

    # def singleNumber(self, nums: List[int]) -> int:
    #     s = set()
    #     for n in nums:
    #         if n not in s:
    #             s.add(n)
    #         else:
    #             s.remove(n)

    #     return s.pop()


if __name__ == "__main__":
    nums = [2, 2, 1]
    sol = Solution()
    print(sol.singleNumber(nums))
