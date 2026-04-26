from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxrate = max(piles)
        minrate = 1
        while minrate < maxrate:
            j = (minrate + maxrate)//2
            start = 0
            for i in piles:
                start += ceil(i/j)
            if start > h:
                minrate = j + 1
                continue
            else:
                maxrate = j
        return minrate


        

        

        