class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        x = sorted(nums)
        final = []
        for i in range(0, len(x) - 1):
            if i != 0 and x[i-1] == x[i]:
                continue
            left = i + 1
            right = len(x) - 1
            while left < right:
                tot = x[left] + x[i] + x[right]
                if left != i+1 and x[left - 1] == x[left]:
                    left += 1
                    continue
                if tot == 0:
                    final.append([x[left], x[i], x[right]])
                    left += 1
                    right -= 1
                    continue
                if tot < 0:
                    left += 1
                    continue
                if tot > 0:
                    right -= 1
                    continue
        return final
        
                    
        