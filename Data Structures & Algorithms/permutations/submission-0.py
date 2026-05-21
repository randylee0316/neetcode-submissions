class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(chosen):
            if len(subset) == len(nums):
                res.append(subset.copy())
            
            for i in range(len(nums)):
                if chosen[i] == False:
                    subset.append(nums[i])
                    chosen[i] = True
                    dfs(chosen)
                    subset.pop()
                    chosen[i] = False
                
        dfs([False for _ in range(len(nums))])

        
        return res
            
