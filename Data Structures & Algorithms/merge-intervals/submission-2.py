class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        new = intervals[0]
        for f, l in intervals:
            if new[1] >= f:
                new = [new[0],
                max(new[1], l)]
            else:
                res.append(new)
                new = [f, l]
        res.append(new)
        return res 