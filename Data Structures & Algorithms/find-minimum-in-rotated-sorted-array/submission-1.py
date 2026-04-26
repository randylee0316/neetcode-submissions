class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < nums[left]: 
                right = mid
            elif nums[mid] > nums[left]:
                if nums[right] > nums[left]:
                    return nums[left]
                else:
                    left = mid + 1
            else:
                return min(nums[mid], nums[right])




        




        