class Solution:
    def permuteUnique(self, nums):
        ans = [[]]

        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    print(new_ans)
                    if i < len(l) and l[i] == n:
                        break
            ans = new_ans
        return ans

    # def permuteUnique(self, nums):
    #     if not nums:
    #         return []

    #     if len(nums) == 1:
    #         return [nums]

    #     sol = []
    #     for i in range(len(nums)):
    #         res = nums[:i] + nums[i+1:]
    #         for p in self.permute(res):
    #             if p + [nums[i]] not in sol:
    #                 sol.append(p + [nums[i]])

    #     return sol
if __name__ == "__main__":
    nums = [1, 1, 3]

    sol = Solution()
    print(sol.permuteUnique(nums))
