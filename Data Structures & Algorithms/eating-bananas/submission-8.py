class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        lower = 1
        while lower < upper:
            mid = (lower + upper)//2
            total = 0
            for i in piles:
                total += (i+mid-1)//mid
            if total <= h:
                upper = mid
            else:
                lower = mid+1
        return lower