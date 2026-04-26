class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        l, r = 0, len(heights) - 1

        while l < r:

            water = (r-l)*min(heights[r], heights[l])
            if water > max:
                max = water
            if heights[r] <= heights[l]:
                r -= 1
            if heights[r] > heights[l]:
                l += 1
        return max


        