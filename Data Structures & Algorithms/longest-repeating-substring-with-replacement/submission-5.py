class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, r, m, e = 0, 0, 0, 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            m = max(m, count[s[r]])
            while r-l + 1 -m> k:
                count[s[l]] -= 1
                l += 1
            e = max(e, r-l+1)
            r+=1
        return e