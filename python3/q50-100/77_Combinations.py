from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        stack = []
        x = 1

        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])

            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1

            else:
                stack.append(x)
                x += 1

    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     combs = [[]]

    #     for _ in range(k):
    #         combs = [
    #             [i] + c for c in combs for i in range(1, c[0] if c else n + 1)
    #         ]

    #     return combs


if __name__ == "__main__":
    n, k = 4, 2
    sol = Solution()
    print(sol.combine(n, k))
