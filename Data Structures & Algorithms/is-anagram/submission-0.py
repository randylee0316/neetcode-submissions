class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        f = defaultdict(int)
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            d[s[i]] += 1
            f[t[i]] += 1

        return d == f
        