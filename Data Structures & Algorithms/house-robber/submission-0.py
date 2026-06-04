class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        prev, curr = nums[0], max(nums[0], nums[1])

        for i in range(3, len(nums) + 1):
            prev, curr = curr, max(curr, prev + nums[i-1])
        
        return curr