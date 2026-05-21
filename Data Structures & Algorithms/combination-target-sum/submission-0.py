class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if sum(subset) > target:
                return
            if sum(subset) == target:
                res.append(subset.copy())
                return
            for ind in range(i, len(nums)):
                subset.append(nums[ind])
                dfs(ind)
                subset.pop()
        
        dfs(0)

        return res