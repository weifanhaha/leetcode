from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0
        for n in nums:
            ones = (ones ^ n) & ~twos
            twos = (twos ^ n) & ~ones
        return ones

    # def singleNumber(self, nums: List[int]) -> int:
    #     # with extra memory
    #     dic = set()
    #     result = set(nums)
    #     for n in nums:
    #         if n not in dic:
    #             dic.add(n)
    #         elif n in dic and n in result:
    #             result.remove(n)

    #     return result.pop()


if __name__ == '__main__':
    l = [0, 1, 0, 1, 0, 1, 99]
    sol = Solution()
    print(sol.singleNumber(l))
