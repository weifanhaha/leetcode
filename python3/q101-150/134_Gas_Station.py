from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, end = len(gas) - 1, 0
        tank = gas[start] - cost[start]
        while start > end:
            if tank >= 0:
                tank += (gas[end] - cost[end])
                end += 1
            else:
                start -= 1
                tank += (gas[start] - cost[start])

        return start if tank >= 0 else -1

    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     # brute force
    #     for i in range(len(gas)):
    #         remain_gas = 0
    #         fin = True
    #         for j in range(len(gas)):
    #             idx = (i+j) % len(gas)
    #             remain_gas += gas[idx]
    #             if remain_gas < cost[idx]:
    #                 fin = False
    #                 break
    #             else:
    #                 remain_gas -= cost[idx]
    #         if fin:
    #             return i

    #     return -1


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    sol = Solution()
    print(sol.canCompleteCircuit(gas, cost))
