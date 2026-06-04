class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev, curr = 0, 0
        prev1, curr1 = 0, 0

        for n in range(1, len(nums)):
            prev, curr = curr, max(curr, prev + nums[n])
        for n in range(1, len(nums)):
            prev1, curr1 = curr1, max(curr1, prev1 + nums[n-1])
        
        return max(curr, curr1)