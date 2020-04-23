from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmpstr(s1, s2):
            return s1 + s2 > s2 + s1

        def mergeSort(nums, l, r):
            if l > r:
                return
            if l == r:
                return [nums[l]]

            mid = (l + r) // 2
            left = mergeSort(nums, l, mid)
            right = mergeSort(nums, mid + 1, r)

            return merge(left, right)

        def merge(left, right):
            i, j, ret = 0, 0, []
            while i < len(left) and j < len(right):
                if cmpstr(left[i], right[j]):
                    ret.append(left[i])
                    i += 1
                else:
                    ret.append(right[j])
                    j += 1

            return ret + (left[i:] or right[j:])

        snums = [str(n) for n in nums]
        return ''.join(mergeSort(snums, 0, len(snums) - 1)).lstrip('0') or '0'


if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    nums = [0, 0, 0]
    sol = Solution()
    print(sol.largestNumber(nums))
