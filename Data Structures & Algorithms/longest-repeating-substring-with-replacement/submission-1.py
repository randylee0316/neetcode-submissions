class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        m = 0
        x = dict()
        for i in range(len(s)):
            x[s[i]] = x.get(s[i], 0) + 1
            if x != {}:
                while i-l + 1 - max(x.values()) > k:
                    x[s[l]] -= 1
                    l += 1
            m = max(m, i-l+1)

        return m
            
            
            

        