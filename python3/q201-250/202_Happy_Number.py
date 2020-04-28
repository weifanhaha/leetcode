class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n not in nums:
            nums.add(n)
            n = self.sum_square(n)
            if n == 1:
                return True
        return False

    def sum_square(self, n):
        i = 0
        while n:
            i += (n % 10) ** 2
            n //= 10
        return i


if __name__ == "__main__":
    sol = Solution()
    n = 19
    print(sol.isHappy(n))
