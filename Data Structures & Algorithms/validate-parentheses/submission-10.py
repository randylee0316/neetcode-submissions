class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        d = {")":"(", "}":"{", "]":"["}
        l = []

        for i in range(len(s)):
            if len(l) == 0 or l[-1] != d.get(s[i], 0):
                l.append(s[i])
                continue
            l.pop()
        
        return len(l) == 0
        
            

        