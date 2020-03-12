class Solution:
    def generateParenthesis(self, n):
        def generate(p, left, right, ans=[]):
            if left:
                generate(p + "(", left-1, right, ans)
            if right > left:
                generate(p + ")", left, right-1, ans)
            if not right:
                ans.append(p)
            return ans
        return generate("", n, n, [])


if __name__ == "__main__":
    n = 3
    sol = Solution()
    ans = sol.generateParenthesis(n)
    print(ans)
