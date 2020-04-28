class Solution:
    def longestPalindrome(self, s):
        res = ''
        for i in range(len(s)):
            # odd
            tmp = self.expand(s, i, i)
            res = tmp if len(tmp) > len(res) else res
            # even
            tmp = self.expand(s, i, i+1)
            res = tmp if len(tmp) > len(res) else res

        return res

    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    # def longestPalindrome(self, s: str) -> str:
    #     dp = [[0] * len(s) for _ in range(len(s))]
    #     max_len = 0
    #     ans = ""

    #     for i in range(len(s) - 1, -1, -1):
    #         for j in range(i, len(s)):
    #             if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1] == 1):
    #                 dp[i][j] = 1
    #                 if j - i + 1 > max_len:
    #                     ans = s[i:j+1]
    #                     max_len = j - i + 1

    #     return ans


if __name__ == "__main__":
    s = "aaaa"
    sol = Solution()
    ans = sol.longestPalindrome(s)
    print(ans)
