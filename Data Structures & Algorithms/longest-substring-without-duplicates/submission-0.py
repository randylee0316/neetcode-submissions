class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        x = set()
        m = 0
        while r < len(s):
            while s[r] in x:
                x.remove(s[l])
                l += 1
            x.add(s[r])
            m = max(m, r-l+1)
            r += 1
        return m