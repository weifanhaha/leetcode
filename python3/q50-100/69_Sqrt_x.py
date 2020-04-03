class Solution:
    # O(log(N)), Newton
    def mySqrt(self, x: int) -> int:
        r = x
        while r * r > x:
            r = (r + x/r) // 2
        return int(r)

    # O(log(N)), binary search
    # def mySqrt(self, x: int) -> int:
    #     if x == 0:
    #         return 0

    #     l, r = 1, x
    #     ans = 1

    #     while l <= r:
    #         mid = (l + r) // 2

    #         if (mid * mid <= x):
    #             l = mid + 1
    #             ans = mid

    #         else:
    #             r = mid - 1

    #     return ans

    # O(N), Brute Force
    # def mySqrt(self, x: int) -> int:
    #     i = 0
    #     while i <= x:
    #         if i * i <= x and (i+1) * (i+1) > x:
    #             return i
    #         i += 1


if __name__ == "__main__":
    x = int(input())
    sol = Solution()
    print(sol.mySqrt(x))
