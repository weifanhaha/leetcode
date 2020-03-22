class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        ret = 1
        while n > 0:
            if n % 2:
                ret *= x
            x *= x
            n //= 2

        return ret

        # if not n:
        #     return 1
        # if n < 0:
        #     return 1 / self.myPow(x, -n)
        # if n % 2:
        #     return x * self.myPow(x, n-1)
        # else:
        #     return self.myPow(x*x, n/2)


if __name__ == "__main__":
    x = 2
    n = -3
    sol = Solution()
    print(sol.myPow(x, n))
