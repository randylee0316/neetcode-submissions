"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.end)
        prev = float('-inf')
        for interval in intervals:
            i, j = interval.start, interval.end
            if i < prev:
                return False
            prev = j
        return True
        
        
