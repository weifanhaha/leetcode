class Solution:
    def trailingZeroes(self, n: int) -> int:
        r = 0
        while n > 0:
            n //= 5
            r += n

        return r


if __name__ == "__main__":
    n = int(input())
    sol = Solution()
    print(sol.trailingZeroes(n))
