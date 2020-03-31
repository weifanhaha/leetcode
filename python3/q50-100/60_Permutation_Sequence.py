import math


class Solution:

    def getPermutation(self, n, k):
        numbers = list(range(1, n+1))
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation

    # TLE
    # def getPermutation(self, n: int, k: int) -> str:
    #     permutations = self.permutate([str(i) for i in range(1, n+1)])

    #     return ''.join(sorted(permutations)[k-1])

    # def permutate(self, nums):
    #     if nums == []:
    #         return []
    #     if len(nums) == 1:
    #         return [nums]

    #     ret = []
    #     for i in range(len(nums)):
    #         res = nums[:i] + nums[i+1:]
    #         for p in self.permutate(res):
    #             ret.append(p + [nums[i]])

    #     return ret


if __name__ == "__main__":
    n = 3
    k = 3
    sol = Solution()
    print(sol.getPermutation(n, k))
