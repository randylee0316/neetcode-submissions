class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)        
        d = defaultdict(list)

        for i in s:
            if i-1 not in s:
                d[i].append(i)
                j = i+1
                while j in s:
                    d[i].append(j)
                    j += 1
        
        return len(max(d.values(), key = len))


        