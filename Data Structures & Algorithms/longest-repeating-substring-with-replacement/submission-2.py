class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        r  = 0
        m = 0
        e = 0
        while r < len(s):
            count[s[r]] = 1+count.get(s[r], 0)
            m = max(m, count[s[r]])
            while r-l+1 - m > k:
                count[s[l]] -= 1
                l += 1
            e = max(e, r-l+1)
            r += 1
        return e