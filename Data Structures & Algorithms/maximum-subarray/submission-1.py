class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, maximum = 0, float('-inf')

        for num in nums:
            if curr < 0:
                curr = num
                maximum = max(curr, maximum)
                continue
            curr += num
            maximum = max(curr, maximum)
        return maximum



