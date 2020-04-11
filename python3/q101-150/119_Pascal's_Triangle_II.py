from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = [1]

        for _ in range(rowIndex):
            ret = [x+y for x, y in zip([0] + ret, ret + [0])]

        return ret


if __name__ == '__main__':
    rowIndex = int(input())
    sol = Solution()
    print(sol.getRow(rowIndex))
