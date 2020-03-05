class Solution:
    def romanToInt(self, s: str) -> int:

        dic = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        ret = 0

        for i, c in enumerate(s):
            if i < len(s) - 1 and dic[c] < dic[s[i+1]]:
                ret -= dic[c]
            else:
                ret += dic[c]
        return ret


if __name__ == "__main__":
    s = "IV"

    sol = Solution()
    ans = sol.romanToInt(s)
    print(ans)
