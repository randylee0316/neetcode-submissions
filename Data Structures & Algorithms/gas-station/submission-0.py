class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        start = 0
        while start < len(cost):
            org = start
            cur = start
            rem = gas[start]
            beg = True

            while rem >= cost[cur]:
                if cur == org and not beg:
                    return start

                rem -= cost[cur]
                cur = (cur + 1) % len(gas)
                rem += gas[cur]
                beg = False
            start += 1
        return -1
            