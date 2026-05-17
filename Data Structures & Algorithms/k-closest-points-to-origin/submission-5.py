class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []
        distances = []

        for i in points:
            x, y = i
            d = math.sqrt(x**2 + y**2)
            heapq.heappush(distances, (d, [x, y]))
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(distances)[1])
        return res
