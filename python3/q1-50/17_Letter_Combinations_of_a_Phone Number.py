from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }

        if (len(digits) == 0):
            return []
        if (len(digits) == 1):
            return [c for c in dic[digits]]
        else:
            prev = self.letterCombinations(digits[:-1])
            last = dic[digits[-1]]
            return [c + tail for c in prev for tail in last]


if __name__ == "__main__":
    digits = "27"
    sol = Solution()
    ans = sol.letterCombinations(digits)
    print(ans)
