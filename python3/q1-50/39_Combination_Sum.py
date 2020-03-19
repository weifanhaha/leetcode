class Solution:
    def combinationSum(self, candidates, target):
        sol = []
        candidates.sort()

        def dfs(sol, candidates, remain, stack=[]):
            if remain == 0:
                sol.append(stack)
                return

            for num in candidates:
                if num > remain:
                    break
                elif stack and num < stack[-1]:
                    continue
                else:
                    dfs(sol, candidates, remain - num, stack + [num])

        dfs(sol, candidates, target)
        return sol


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    sol = Solution()
    print(sol.combinationSum(candidates, target))
