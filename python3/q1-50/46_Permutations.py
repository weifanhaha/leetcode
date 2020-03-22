class Solution:
    def permute(self, nums):
        if not nums:
            return []

        if len(nums) == 1:
            return [nums]

        sol = []
        for i in range(len(nums)):
            res = nums[:i] + nums[i+1:]
            for p in self.permute(res):
                sol.append(p + [nums[i]])

        return sol


if __name__ == "__main__":
    nums = [1, 2, 3]

    sol = Solution()
    print(sol.permute(nums))
