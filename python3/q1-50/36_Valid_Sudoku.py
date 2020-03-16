class Solution(object):
    def isValidSudoku(self, board):
        return self.is_valid_row(board) and \
            self.is_valid_col(board) and \
            self.is_valid_square(board)

    def is_valid_row(self, board):
        for row in board:
            nums = set()
            for n in row:
                if n not in nums or n == ".":
                    nums.add(n)
                else:
                    return False
        return True

    def is_valid_col(self, board):
        nums_list = [set() for i in range(len(board))]
        for row in board:
            for n in range(len(row)):
                if row[n] not in nums_list[n] or row[n] == ".":
                    nums_list[n].add(row[n])
                else:
                    return False
        return True

    def is_valid_square(self, board):
        def check_square(board, corner):
            nums = set()
            for x in range(corner[0], corner[0]+3):
                for y in range(corner[1], corner[1]+3):
                    if board[x][y] not in nums or board[x][y] == ".":
                        nums.add(board[x][y])
                    else:
                        return False
            return True

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not check_square(board, (i, j)):
                    return False

        return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    sol = Solution()
    print(sol.isValidSudoku(board))
