class Solution:
    def longestValidParentheses(self, s: str) -> int:

        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2 if i >= 2 else 2
                if s[i-1] == ")":
                    if i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == "(":
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        print(dp)
        return max(dp) if dp else 0


if __name__ == "__main__":
    s = "(()))())("
    sol = Solution()
    ans = sol.longestValidParentheses(s)
    print(ans)
