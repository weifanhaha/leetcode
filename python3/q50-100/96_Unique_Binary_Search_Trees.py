class Solution:
    # bottom up dp
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1

        dp = [0] * (1+n)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = sum([
                dp[sep] * dp[i-sep-1] for sep in range(i)
            ])

        return dp[n]
