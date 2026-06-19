class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        res = 0
        prev = intervals[0][1]
        for x in range(1, len(intervals)):
            i, j = intervals[x]
            if i < prev:
                prev = min(prev, j)

                res += 1
            else:
                prev = j
        
                
        return res
