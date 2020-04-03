from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]

        # initialize
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j == 0:
                        continue
                    dp[i][j] = dp[i][j-1]

                elif j == 0:
                    if i == 0:
                        continue
                    dp[i][j] = dp[i-1][j]

                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

                if obstacleGrid[i][j]:
                    dp[i][j] = 0

        return dp[m-1][n-1]

    # TLE
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     n, m = len(obstacleGrid), len(obstacleGrid[0])
    #     if obstacleGrid[0][0] == 1 or obstacleGrid[n-1][m-1] == 1:
    #         return 0

    #     def dfs(path, i, j):
    #         if (i == n-1 and j == m-1):
    #             return path + 1

    #         if i < n-1 and not obstacleGrid[i+1][j]:
    #             path = dfs(path, i+1, j)

    #         if j < m-1 and not obstacleGrid[i][j+1]:
    #             path = dfs(path, i, j+1)

    #         return path

    #     return dfs(0, 0, 0)


if __name__ == "__main__":
    obstacleGrid = [
        [0, 1, 0],
    ]
    sol = Solution()
    print(sol.uniquePathsWithObstacles(obstacleGrid))
