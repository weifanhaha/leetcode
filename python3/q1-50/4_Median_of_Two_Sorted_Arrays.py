from typing import List

# Try log(m+n) later


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        is_odd = total_len % 2
        mid = int(total_len/2) + 1

        INT_MAX = 999999999
        nums1.append(INT_MAX)
        nums2.append(INT_MAX)

        i = j = 0
        buf = []
        while (i < len(nums1) or j < len(nums2)):
            if j >= len(nums2) or (nums1[i] < nums2[j]):
                buf.append(nums1[i])
                i += 1
            else:
                buf.append(nums2[j])
                j += 1
            if len(buf) >= mid:
                return buf[-1] if is_odd else (buf[-2] + buf[-1]) / 2


if __name__ == "__main__":
    nums1 = [1]
    nums2 = [0]

    sol = Solution()
    ans = sol.findMedianSortedArrays(nums1, nums2)
    print(ans)
