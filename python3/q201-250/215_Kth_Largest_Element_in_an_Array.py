import heapq


class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for i in range(k):
            heapq.heappush(nums[i])

        for n in nums[k:]:
            if n > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, n)

        return heap[0]

    # O(NlgN)
    # def findKthLargest(self, nums, k):
    #     return sorted(nums, reverse=True)[k-1]
    # def findKthLargest(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     def find_medians(X):
    #         i = 0
    #         medians = []
    #         while i < len(X):
    #             subX = X[i:i+5]
    #             mid = len(subX) // 2
    #             medians.append(sorted(subX)[mid])
    #             i += 5
    #         return medians

    #     if len(nums) <= 5:
    #         return sorted(nums)[len(nums)-k]

    #     else:
    #         M = find_medians(nums)
    #         MoM = self.findKthLargest(M, len(M)//2 + 1)

    #         X1 = []
    #         X2 = []

    #         for i in range(len(nums)):
    #             if nums[i] < MoM:
    #                 X1.append(nums[i])
    #             else:
    #                 X2.append(nums[i])
    #         # get rid of MoM itself
    #         X2.remove(MoM)

    #         if len(X2) == k - 1:   # MoM is kth large number
    #             return MoM
    #         if len(X2) > k - 1:   # kth large number in k>MoM group
    #             return self.findKthLargest(X2, k)
    #         # kth large number in k<MoM group
    #         return self.findKthLargest(X1, k-len(X2)-1)


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 4
    sol = Solution()
    print(sol.findKthLargest(nums, k))
