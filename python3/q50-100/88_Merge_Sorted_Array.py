from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        while n > 0:
            if m <= 0 or nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1


if __name__ == '__main__':
    nums1 = [1, 7, 0, 0, 0]
    m = 2
    nums2 = [1, 2, 9]
    n = 3

    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print(nums1)
