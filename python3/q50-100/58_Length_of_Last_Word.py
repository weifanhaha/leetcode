class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        word_list = s.strip().split()
        return 0 if not word_list else len(word_list[-1])


if __name__ == "__main__":
    s = "Hello World"
    sol = Solution()
    print(sol.lengthOfLastWord(s))
