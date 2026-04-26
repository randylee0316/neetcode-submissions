class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        final = []

        l = 0
        r = len(nums) - 1

        while l < r:
            m = l+1
            while m < r:
                if nums[m] + nums[l] + nums[r] < 0:
                    m += 1
                elif nums[m] + nums[l] + nums[r] == 0:
                    if [nums[l],nums[r],nums[m]] not in final:
                        final.append([nums[l],nums[r],nums[m]])
                    m += 1
                    r -= 1
                elif nums[m] + nums[l] + nums[r] > 0:
                    r -= 1
            l += 1
            r = len(nums) - 1
        return final
                
            
        
        
                    
        