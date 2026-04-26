class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = list(zip(position, speed))
        s.sort(key = lambda x: x[0], reverse = True)
        t = []
        for p, s in s:
            time = (target - p)/s
            if not t or t[-1] < time:
                t.append(time)
        return len(t)
