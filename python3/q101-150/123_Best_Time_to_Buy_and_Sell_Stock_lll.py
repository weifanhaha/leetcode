from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price1 = min_price2 = float('inf')
        max_profit1 = max_profit2 = 0
        for p in prices:
            min_price1 = min(min_price1, p)
            max_profit1 = max(max_profit1, p - min_price1)
            min_price2 = min(min_price2, p - max_profit1)
            max_profit2 = max(max_profit2, p - min_price2)

        return max_profit2


if __name__ == "__main__":
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    sol = Solution()
    print(sol.maxProfit(prices))
