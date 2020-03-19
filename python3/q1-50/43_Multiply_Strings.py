class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        i_num1 = self.strs2ints(num1)
        i_num2 = self.strs2ints(num2)

        return self.ints2strs(i_num1*i_num2)

    def strs2ints(self, s_num):
        loc = 0
        num = 0
        while loc < len(s_num):
            n = self.str2int(s_num[loc])
            num += n * 10**(len(s_num)-loc-1)
            loc += 1
        return num

    def str2int(self, s):
        return ord(s)-ord("0")

    def ints2strs(self, i_num):
        s_num = ""
        while i_num > 0:
            s = self.int2str(i_num % 10)
            s_num = s + s_num
            i_num = i_num // 10
        return s_num

    def int2str(self, i):
        return chr(i+ord("0"))
