class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i


if __name__ == "__main__":
    m, n = 5, 7
    sol = Solution()
    print(sol.rangeBitwiseAnd(m, n))
