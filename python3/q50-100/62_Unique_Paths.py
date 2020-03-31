import math


class Solution:
    def uniquePaths(self, m, n):
        return math.factorial(m+n-2) // (math.factorial(m-1) * math.factorial(n-1))


if __name__ == "__main__":
    m = 3
    n = 7
    sol = Solution()
    print(sol.uniquePaths(m, n))
