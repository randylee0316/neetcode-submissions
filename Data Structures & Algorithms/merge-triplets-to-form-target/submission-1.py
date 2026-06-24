class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        merged = [0, 0, 0]
        for i in range(len(triplets)):
            invalid = False
            for j in range(3):
                if triplets[i][j] > target[j]:
                    invalid = True
                    break
            if invalid:
                continue
            merged = [max(merged[0], triplets[i][0])
                    , max(merged[1], triplets[i][1])
                    , max(merged[2], triplets[i][2])]
        return merged == target