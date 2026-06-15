class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        m = M = 1

        for num in nums:
            tmp_m = m
            tmp_M = M
            m = min(num*tmp_m, num, num*tmp_M)
            M = max(num*tmp_m, num, num*tmp_M)
            res = max(res, M)
        
        return res


