class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n+1)
        # initialize
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

    # recur => may cause TLE
    # def climbStairs(self, n: int) -> int:
    #     def recur(n):
    #         if n == 1:
    #             return 1
    #         if n == 2:
    #             return 2
    #         else:
    #             return recur(n-1) + recur(n-2)

    #     return recur(n)


if __name__ == "__main__":
    n = int(input())
    sol = Solution()
    print(sol.climbStairs(n))
