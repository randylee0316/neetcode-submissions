class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)

        for i in range(len(nums)-2, -1, -1):
            res = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, dp[j])
            dp[i] = res + 1
        
        return max(dp)

