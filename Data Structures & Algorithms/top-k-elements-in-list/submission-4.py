class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for i in nums:
            d[i] += 1
        
        l = [[] for _ in range(len(nums)+1)]
        
        for key, val in d.items():
            l[val].append(key)
        f = []
        for i in reversed(l):
            for j in i:
                f.append(j)
                if len(f) == k:
                    return f
        




        