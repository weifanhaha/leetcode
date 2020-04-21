class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])


if __name__ == "__main__":
    s = "a good   example"
    sol = Solution()
    print(sol.reverseWords(s))
