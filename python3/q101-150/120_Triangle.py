from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return []

        dp = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                dp[i] = row[i] + min(dp[i], dp[i+1])

        return dp[0]


if __name__ == "__main__":
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    sol = Solution()
    print(sol.minimumTotal(triangle))
