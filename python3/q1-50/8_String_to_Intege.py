class Solution:
    def myAtoi(self, s: str) -> int:
        ret = 0
        i = 0
        sign = 1

        while i < len(s) and s[i] == " ":
            i += 1

        if i < len(s) and (s[i] == "+" or s[i] == "-"):
            sign = 1 - 2*(s[i] == "-")
            i += 1

        while (i < len(s) and '0' <= s[i] <= '9'):
            ret = 10 * ret + (ord(s[i]) - ord('0'))
            i += 1

        return max(-2**31, min(sign * ret, 2**31 - 1))

    def myAtoi2(self, s: str) -> int:
        ret = 0
        s = s.strip()

        if s == "":
            return 0
        sign = 1
        if s[0] == "-" or s[0] == "+":
            if s[0] == "-":
                sign = -1
            s = s[1:]
        for c in s:
            if ord('0') <= ord(c) <= ord('9'):
                ret = 10 * ret + (ord(c) - ord('0'))
            else:
                break
        return max(-2**31, min(sign * ret, 2**31 - 1))


if __name__ == "__main__":
    s = " "
    sol = Solution()
    ans = sol.myAtoi(s)
    print(ans)
