from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_pal(s):
            return s == s[::-1]

        def dfs(s, path, res):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s) + 1):
                if is_pal(s[:i]):
                    dfs(s[i:], path + [s[:i]], res)

        res = []
        dfs(s, [], res)
        return res


if __name__ == '__main__':
    s = 'aab'
    sol = Solution()
    print(sol.partition(s))
