class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        d = len(v2) - len(v1)

        for a, b in zip(v1 + ['0'] * d, v2 + ['0'] * (-d)):
            if int(a) > int(b):
                return 1
            elif int(a) < int(b):
                return -1
        return 0


if __name__ == '__main__':
    version1 = "1.0.11"
    version2 = "1.0.12"
    sol = Solution()
    print(sol.compareVersion(version1, version2))
