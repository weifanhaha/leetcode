from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # if not len(matrix) or not len(matrix[0]):
        #     return [[]]

        m, n = len(matrix), len(matrix[0])

        zero_row = set()
        zero_col = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)

        for row in zero_row:
            for j in range(n):
                matrix[row][j] = 0

        for col in zero_col:
            for i in range(m):
                matrix[i][col] = 0


if __name__ == '__main__':
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]

    # matrix = [[1, 0], [1, 1]]

    sol = Solution()
    sol.setZeroes(matrix)
    print(matrix)
