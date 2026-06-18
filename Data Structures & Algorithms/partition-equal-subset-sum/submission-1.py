class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        h = s//2

        dp = [False]*(h + 1)
        dp[0] = True
        for num in nums:
            for i in range(h, num - 1, -1):
                dp[i] = dp[i] or dp[i-num]
        
        return dp[h]

        