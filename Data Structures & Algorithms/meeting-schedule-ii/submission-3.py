"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        res = 0
        prev = float('inf')
        end = []

        for i in intervals:
            if i.start < prev:
                res += 1
                heapq.heappush(end, i.end)
                prev = end[0]
                continue
            heapq.heappop(end)
            heapq.heappush(end, i.end)
            prev = end[0]
        
        return res