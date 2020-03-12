# TLE
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_pos = (dividend > 0) == (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        while dividend - divisor >= 0:
            dividend = dividend - divisor
            ans += 1

        return ans if is_pos else -ans


if __name__ == "__main__":
    dividend = 10
    divisor = 3

    sol = Solution(dividend, divisor)
    print(sol)
