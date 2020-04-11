from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []

        ret = [[1]]

        for _ in range(numRows - 1):
            ret.append([x+y for x, y in zip(ret[-1] + [0], [0] + ret[-1])])
        return ret


if __name__ == '__main__':
    numRows = int(input())
    sol = Solution()
    print(sol.generate(numRows))
