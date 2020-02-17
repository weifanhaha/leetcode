class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        # reverse it and check if the same
        tmp, ret = x, 0
        while tmp:
            ret = ret * 10 + tmp % 10
            tmp //= 10
        return ret == x

    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1] == str(x)


if __name__ == "__main__":
    x = 1001
    sol = Solution()
    print(sol.isPalindrome(x))
