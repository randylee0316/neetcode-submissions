class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])
        if len(cost) == 3:
            return min(cost[1], self.minCostClimbingStairs(cost[:-1]) + cost[-1])
        
        prev, curr = min(cost[0], cost[1]), min(cost[1], self.minCostClimbingStairs(cost[:-1]) + cost[-1])

        for i in range(4, len(cost) + 1):
            prev, curr = curr, min(curr + cost[i-1], prev + cost[i-2]) 
        
        return curr