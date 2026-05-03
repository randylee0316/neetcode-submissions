class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        unique = {}
        for i in t:
            unique[i] = 1 + unique.get(i, 0)
        
        d = {}
        match = 0
        l = 0
        f = []
        for r in range(len(s)):
            char = s[r]
            if char in unique:
                d[char] = d.get(char, 0) + 1
                if d[char] == unique[char]:
                    match += 1
            
            while match == len(unique):
                f.append(s[l : r + 1])
                if s[l] in unique:
                    d[s[l]] -= 1
                    if d[s[l]] < unique[s[l]]:
                        match -= 1
                l += 1
        return min(f, key = len) if f else ""
