from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, i, j, word):
            if word == '':
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
                return False

            tmp = board[i][j]
            board[i][j] = '#'  # visited

            subword = word[1:]
            ret = dfs(board, i+1, j, subword) or dfs(board, i-1, j,
                                                     subword) or dfs(board, i, j+1, subword) or dfs(board, i, j-1, subword)

            board[i][j] = tmp
            return ret

        if not board:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word):
                    return True

        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    sol = Solution()
    print(sol.exist(board, word))
