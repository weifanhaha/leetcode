from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        candidates.sort()

        def dfs(sol, candidates, remain, stack=[]):
            if remain == 0:
                sol.append(stack)
                return

            i = 0
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > remain:
                    break

                dfs(sol, candidates[i+1:], remain -
                    candidates[i], stack + [candidates[i]])

        dfs(sol, candidates, target)
        return sol


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    sol = Solution()
    print(sol.combinationSum2(candidates, target))
