class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False

    #     dic_st = {}
    #     dic_ts = {}

    #     for i in range(len(s)):
    #         if s[i] not in dic_st and t[i] not in dic_ts:
    #             dic_st[s[i]] = t[i]
    #             dic_ts[t[i]] = s[i]
    #         elif (s[i] in dic_st and dic_st[s[i]] != t[i]) or (t[i] in dic_ts and dic_ts[t[i]] != s[i]):
    #             return False
    #     return True


if __name__ == "__main__":
    s = 'qoo'
    t = 'qff'
    sol = Solution()
    print(sol.isIsomorphic(s, t))
