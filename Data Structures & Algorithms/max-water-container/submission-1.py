class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highest = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            distance = right - left
            vol = min(heights[left], heights[right])*distance
            if vol > highest:
                highest = vol
            if heights[left] < heights[right]:
                left += 1
                continue
            if heights[right] < heights[left]:
                right -= 1
                continue
            left += 1
            right -= 1
            
        return highest



        