class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        mi = prices[0]
        for i in prices:
            m = max(m, i - mi)
            mi = min(i, mi)
        return m
            



        