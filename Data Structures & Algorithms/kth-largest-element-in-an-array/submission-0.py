class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = []

        for i in nums:
            heapq.heappush(l, i)
            if len(l) > k:
                heapq.heappop(l)
        
        return l[0]

