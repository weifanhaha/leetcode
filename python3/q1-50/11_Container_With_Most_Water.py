from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1

        max_area = 0
        while l < r:
            max_area = max(max_area, (r-l) * min(height[l], height[r]))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return max_area


if __name__ == "__main__":
    height = [1, 2, 8, 4, 5]

    sol = Solution()
    ans = sol.maxArea(height)
    print(ans)
