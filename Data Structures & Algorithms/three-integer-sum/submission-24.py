class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        f = []
        
        nums.sort()

        for i, v in enumerate(nums):
            if v > 0:
                break
            
            if i > 0 and v == nums[i - 1]:
                continue

            m, r = i+1, len(nums) - 1
            while m < r:
                if nums[i] + nums[m] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[m] + nums[r] < 0:
                    m += 1
                else:
                    f.append([nums[i], nums[m], nums[r]])
                    while nums[i] + nums[m] + nums[r] == 0 and m < r:
                        m += 1
                    r -= 1
        return f