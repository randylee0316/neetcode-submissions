class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        d = {}
        for num in hand:
            d[num] = d.get(num, 0) + 1
        heap = hand.copy()
        heapq.heapify(heap)

        for j in range(len(hand) // groupSize):
            while heap and d[heap[0]] == 0:
                heapq.heappop(heap)

            if not heap:
                return False

            m = heapq.heappop(heap)

            for i in range(groupSize):
                if m + i not in d or d[m + i] == 0:
                    return False
                d[m + i] -= 1

        return True



                
            
            
