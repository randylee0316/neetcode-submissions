class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 1
        m = 0
        while s < len(prices):
            if prices[s] - prices[b] > 0:
                m = max(m, prices[s] - prices[b])
            else:
                b =s
            s += 1
        return m

