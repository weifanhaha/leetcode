from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        sorted_i = sorted(intervals, key=lambda x: x[0])

        res = [sorted_i[0]]
        for interval in sorted_i[1:]:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)

        return res

    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     sorted_i = sorted(intervals, key=lambda x: x[0])
    #     merged = []

    #     i = 0

    #     while i < len(sorted_i):
    #         curr = sorted_i[i]
    #         while i < len(sorted_i) - 1 and sorted_i[i+1][0] <= curr[1]:
    #             curr = [min(curr[0], sorted_i[i+1][0]),
    #                     max(curr[1], sorted_i[i+1][1])]
    #             i += 1
    #         merged.append(curr)

    #         i += 1
    #     return merged


if __name__ == "__main__":
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # intervals = [[1, 3], [8, 10], [15, 18], [2, 6]]
    # intervals = [[1, 4], [4, 5]]
    intervals = [[1, 4], [2, 3]]

    sol = Solution()
    print(sol.merge(intervals))
