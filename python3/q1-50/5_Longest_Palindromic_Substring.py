class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for _ in range(len(s))]
        max_len = 0
        ans = ""

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    if j - i + 1 > max_len:
                        ans = s[i:j+1]
                        max_len = j - i + 1

        return ans


if __name__ == "__main__":
    s = "aaaa"
    sol = Solution()
    ans = sol.longestPalindrome(s)
    print(ans)
