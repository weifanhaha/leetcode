class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # binary search for row
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True

            if matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1

        row = (l + r) // 2

        # binary search for col
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True

            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False


if __name__ == '__main__':
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50],
        [52, 55, 60, 70],
    ]

    matrix = [[0, 1], [2, 4]]

    target = 4

    sol = Solution()
    print(sol.searchMatrix(matrix, target))


# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if len(matrix) == 0 or len(matrix[0]) == 0:
#             return False

#         new_list = []
#         for line in matrix:
#             new_list = new_list + line

#         low = 0
#         high = len(new_list) - 1

#         while low <= high:
#             mid = (low + high) // 2
#             print(low, mid, high)
#             if new_list[mid] == target:
#                 return True
#             elif target > new_list[mid]:
#                 low = mid+1
#             elif target < new_list[mid]:
#                 high = mid-1

#         return False
