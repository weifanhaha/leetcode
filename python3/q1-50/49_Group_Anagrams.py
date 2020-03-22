class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        group = {}
        for s in strs:
            chars = ''.join(sorted(s))
            if chars in group:
                group[chars].append(s)
            else:
                group[chars] = [s]

        return list(group.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    print(sol.groupAnagrams(strs))
