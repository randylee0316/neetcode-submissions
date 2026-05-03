class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        perm = {}
        for i in s1:
            perm[i] = 1+perm.get(i, 0)
        
        comp = {}
        l = 0
        r = len(s1)-1
        for i in range(len(s1)):
            comp[s2[i]] = 1+comp.get(s2[i], 0)
        while r < len(s2):
            if perm == comp:
                return True
            else:
                if comp[s2[l]] == 1:
                    comp.pop(s2[l])
                else:
                    comp[s2[l]] -= 1
            l += 1
            r += 1
            if r < len(s2):
                comp[s2[r]] = 1+comp.get(s2[r], 0)
        return False

        