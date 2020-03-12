from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def ksum(nums, k, target):
            i = 0
            result = set()

            if k == 2:
                j = len(nums) - 1
                while i < j:
                    if nums[i] + nums[j] == target:
                        result.add((nums[i], nums[j]))
                        i += 1
                    elif nums[i] + nums[j] > target:
                        j -= 1
                    else:
                        i += 1
            else:
                while i < len(nums) - k + 1:
                    subsum = ksum(nums[i+1:], k-1, target-nums[i])
                    if subsum:
                        result = result | set(
                            (nums[i],) + subn for subn in subsum)
                    i += 1
            return result

        nums.sort()
        return [list(s) for s in ksum(nums, 4, target)]


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0

    sol = Solution()
    ans = sol.fourSum(nums, target)
    print(ans)
