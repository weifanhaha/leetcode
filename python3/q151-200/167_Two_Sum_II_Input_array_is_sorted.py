from typing import List


class Solution:
    # O(N), O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i+1, j+1]

    # O(N), O(N)
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     dic = {}
    #     for i, n in enumerate(numbers):
    #         if n in dic:
    #             return [dic[n], i+1]

    #         dic[target - n] = i+1


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.twoSum(numbers, target))
