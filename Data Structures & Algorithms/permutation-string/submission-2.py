class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = dict()
        for i in s1:
            d[i] = d.get(i, 0) + 1
        x = dict()
        for i in s2[:len(s1)]:
            x[i] = x.get(i, 0) + 1
        if x == d:
            return True
        for i in range(len(s2) - len(s1)):
            x[s2[i]] -= 1
            x[s2[i+len(s1)]] = x.get(s2[i+len(s1)], 0) + 1
            if x[s2[i]] == 0:
                x.pop(s2[i])
            if x == d:
                return True
        return False




        