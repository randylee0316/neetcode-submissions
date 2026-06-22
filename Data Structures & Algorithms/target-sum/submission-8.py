class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        l = len(nums)
        dp = [defaultdict(int) for _ in range(l + 1)]
        dp[0][0] = 1

        for i in range(len(nums)):
            for s, w in dp[i].items():
                dp[i+ 1][s + nums[i]] += w
                dp[i + 1][s - nums[i]] += w 
        
        return dp[l][target]