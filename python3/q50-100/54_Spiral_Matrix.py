from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix and matrix[0]:
            # pop the top of the matrix and append to ans
            ans += [*matrix.pop(0)]

            # rotate 90 degree counter-clockwise
            flip_m = [[*reversed(l)] for l in matrix]
            matrix = [*zip(*flip_m)]

        return ans

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]:
#             return []

#         t = l = 0
#         b = len(matrix) - 1
#         r = len(matrix[0]) - 1

#         ans = []

#         while b > t and r > l:
#             ans += [matrix[t][j] for j in range(l, r)]
#             ans += [matrix[i][r] for i in range(t, b)]
#             ans += [matrix[b][j] for j in range(r, l, -1)]
#             ans += [matrix[i][l] for i in range(b, t, -1)]

#             t, l, b, r = t + 1, l + 1, b - 1, r - 1

#         # thin matrix
#         if l == r:
#             ans += [matrix[i][r] for i in range(t, b+1)]

#         # fat matrix
#         elif t == b:
#             ans += [matrix[t][j] for j in range(l, r+1)]
#         return ans


if __name__ == "__main__":
    # matrix = [[1]]
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    # matrix = [
    #     [1, 2, 3, 4],
    #     [5, 6, 7, 8],
    #     [9, 10, 11, 12]
    # ]
    sol = Solution()
    print(sol.spiralOrder(matrix))
