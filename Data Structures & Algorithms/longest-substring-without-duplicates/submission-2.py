class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = 1
        m = 1
        unique = set(s[l])
        while r < len(s):
            if s[r] not in unique:
                m = max(m, r-l+1)
                unique.add(s[r])
            else:
                while s[r] in unique:
                    unique.remove(s[l])
                    l += 1
                unique.add(s[r])
            r += 1
        return m