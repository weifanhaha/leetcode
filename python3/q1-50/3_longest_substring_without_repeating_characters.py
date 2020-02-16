class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        max_len = 0
        chars = set()
        while l <= r and r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                max_len = max(max_len, r - l + 1)
                r += 1
            else:
                chars.remove(s[l])
                l += 1
        return max_len


if __name__ == "__main__":
    sol = Solution()
    s = "aa"
    ans = sol.lengthOfLongestSubstring(s)
    print(ans)
