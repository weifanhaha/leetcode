from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        short = min(strs, key=len)
        for i, c in enumerate(short):
            for s in strs:
                if s[i] != c:
                    return s[:i]
        return short
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if len(strs) < 1:
    #         return ""

    #     min_len = min([len(s) for s in strs])
    #     i = 0

    #     while True:
    #         if i >= min_len:
    #             return strs[0][:i]
    #         c = strs[0][i]
    #         for s in strs:
    #             if i < len(s) and s[i] != c:
    #                 return s[:i]

    #         i += 1


if __name__ == "__main__":
    strs = ["dog", "do"]

    sol = Solution()
    ans = sol.longestCommonPrefix(strs)
    print(ans)
