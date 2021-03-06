from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # edge case
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        # initialize
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        print(dp)

        return dp[m-1][n-1]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

    grid = [[1, 2], [3, 3]]

    sol = Solution()
    print(sol.minPathSum(grid))
