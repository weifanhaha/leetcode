class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pair = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in pair.values():
                stack.append(c)
            elif stack == [] or c not in pair or pair[c] != stack.pop():
                return False

        return stack == []


if __name__ == "__main__":
    s = ''
    sol = Solution()
    print(sol.isValid(s))
