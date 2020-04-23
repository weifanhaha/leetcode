from typing import List


class Solution:
    # O(N), O(1)
    def majorityElement(self, nums: List[int]) -> int:
        count, cand = 0, 0
        for num in nums:
            if num == cand:
                count += 1
            elif count == 0:
                cand, count = num, 1
            else:
                count -= 1
        return cand
    # O(N), O(N)
    # def majorityElement(self, nums: List[int]) -> int:
    #     dic = {}
    #     thres = len(nums) // 2
    #     for n in nums:
    #         if n in dic:
    #             dic[n] = dic[n] + 1
    #         else:
    #             dic[n] = 1
    #         if dic[n] > thres:
    #             return n


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 3, 4, 2]
    sol = Solution()
    print(sol.majorityElement(nums))
