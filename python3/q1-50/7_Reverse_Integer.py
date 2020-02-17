class Solution:
    def reverse(self, x: int) -> int:
        s = 1 if x >= 0 else -1
        x = s * x

        ret = s*int(str(x)[::-1])
        if ret > 2**31-1 or ret < -2**31:
            return 0
        return ret

    def reverse2(self, x: int) -> int:
        s = 1 if x >= 0 else -1
        x = s * x

        ret = 0
        while x:
            ret *= 10
            ret += x % 10
            x = int(x/10)

        if s * ret > 2**31-1 or s * ret < -2**31:
            return 0

        return s * ret


if __name__ == "__main__":
    x = 7463847412
    sol = Solution()
    ans = sol.reverse(x)
    print(ans)
