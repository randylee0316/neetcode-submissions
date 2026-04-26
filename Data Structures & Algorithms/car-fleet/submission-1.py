class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position, speed))
        zipped.sort(key = lambda x: x[0], reverse = True)
        tot_time = []
        for i in range(len(position)):
            x = zipped[i]
            total = (target - x[0])/x[1]
            if tot_time and tot_time[-1] >= total:
                continue
            tot_time.append(total)
        return len(tot_time)
