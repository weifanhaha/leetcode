class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        rows = [''] * numRows

        row, step = 0, 1
        for char in s:
            rows[row] += char
            # move forward
            if row == 0:
                step = 1
            # move backward
            elif row == (numRows - 1):
                step = -1
            row += step
        return ''.join(rows)


if __name__ == "__main__":
    s = "AB"
    numRows = 5
    sol = Solution()
    ans = sol.convert(s, numRows)
    print(ans)
