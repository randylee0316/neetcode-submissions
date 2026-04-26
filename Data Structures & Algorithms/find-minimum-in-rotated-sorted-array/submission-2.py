class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l+r)//2
            if nums[m] < nums[r]:
                r = m
            else:
                if r - l == 1:
                    return nums[r]
                l = m
        return nums[l]