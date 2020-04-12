class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = [c.lower() for c in s if c.isalnum()]
        return l == l[::-1]

    # def isPalindrome(self, s: str) -> bool:
    #     s = s.strip()
    #     i, j = 0, len(s) - 1

    #     while i <= j:
    #         while i < j and not s[i].isalnum():
    #             i += 1
    #         while i < j and not s[j].isalnum():
    #             j -= 1
    #         if s[i].lower() != s[j].lower() or not s[i].isalnum() or not s[j].isalnum():
    #             return False
    #         i, j = i+1, j-1

    #     return True


if __name__ == "__main__":
    s = "  "
    sol = Solution()
    print(sol.isPalindrome(s))
