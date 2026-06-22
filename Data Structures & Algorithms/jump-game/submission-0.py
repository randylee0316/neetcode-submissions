class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = True
        minpos = len(nums) - 1
        for i in range(2, len(nums)+1):
            if nums[-i] >= minpos- (len(nums) - i):
                minpos = len(nums) - i
            
        return minpos == 0
            

            