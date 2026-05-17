class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            M = heapq.heappop(stones)
            m = heapq.heappop(stones)
            if M == m:
                continue
            else:
                heapq.heappush(stones, M - m)
        return -stones[0] if stones else 0
        