class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1match = [0]*26
        s2match = [0]*26

        for i in range(len(s1)):
            s1match[ord(s1[i]) - ord('a')] += 1
            s2match[ord(s2[i]) - ord('a')] += 1
        match = 0
        
        for i in range(26):
            match += (1 if s1match[i] == s2match[i] else 0)
        
        l = 0
        r = len(s1)-1

        while r < len(s2):
            if match == 26:
                return True
            if r == len(s2) - 1:
                break
            order1 = ord(s2[l]) - ord('a')
            order2 = ord(s2[r+1]) - ord('a') 
            if s1match[order1] == s2match[order1]:
                match -= 1
            elif s1match[order1] == s2match[order1] - 1:
                match += 1
            s2match[order1] -= 1
            l += 1
            if s1match[order2] == s2match[order2]:
                match -= 1
            elif s1match[order2] == s2match[order2] + 1:
                match += 1
            s2match[order2] += 1
            r += 1
        return False
