class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}

        for i in range(len(s)):
            d[s[i]] = i
        res = []
        num = 0
        last = 0
        for i in range(len(s)):
            num += 1
            last = max(last, d[s[i]])

            if last == i:
                res.append(num)
                num = 0
        return res
