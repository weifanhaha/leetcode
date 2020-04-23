class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ''
        while n:
            s = chr(ord('A') + (n - 1) % 26)
            ans = s + ans
            n = (n-1) // 26

        return ans


if __name__ == "__main__":
    n = int(input())
    sol = Solution()
    print(sol.convertToTitle(n))
