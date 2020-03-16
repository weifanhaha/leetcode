from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        return self.solve()

    def solve(self):
        self.print_board()
        candidates = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for i in range(9):
            for j in range(9):
                if self.board[i][j] != ".":
                    continue
                for n in candidates:
                    if self.is_safe(i, j, n):
                        self.board[i][j] = n
                        if self.solve():
                            return True
                        self.board[i][j] = "."
                return False
        return True

    def is_safe(self, row, col, num):
        for n in self.board[row]:
            if n == num:
                return False

        for r in range(9):
            if self.board[r][col] == num:
                return False

        corner = (row - row % 3, col - col % 3)
        for i in range(corner[0], corner[0]+3):
            for j in range(corner[1], corner[1]+3):
                if self.board[i][j] == num:
                    return False
        return True

    def print_board(self):
        print("===============================================")
        for row in self.board:
            print(row)


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
    print(sol.solveSudoku(board))
    sol.print_board()
