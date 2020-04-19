from typing import List
import collections


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        n_rows = len(board)
        n_cols = len(board[0])
        queue = collections.deque()

        def is_edge(i, j):
            return i == 0 or i == n_rows - 1 or j == 0 or j == n_cols - 1

        # find the 'O' on the edge
        for i in range(n_rows):
            for j in range(n_cols):
                if is_edge(i, j) and board[i][j] == 'O':
                    queue.append((i, j))

        while queue:
            i, j = queue.popleft()
            board[i][j] = 'E'

            for r, c in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= r < n_rows and 0 <= c < n_cols and board[r][c] == 'O':
                    queue.append((r, c))

        for i in range(n_rows):
            for j in range(n_cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'


if __name__ == '__main__':
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

    sol = Solution()
    sol.solve(board)
    print(board)
