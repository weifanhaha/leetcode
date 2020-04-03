class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ret = ''

        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1

            ret += str(carry % 2)
            carry //= 2

        return ret[::-1]


if __name__ == "__main__":
    a = "1010"
    b = "1011"
    sol = Solution()
    print(sol.addBinary(a, b))
