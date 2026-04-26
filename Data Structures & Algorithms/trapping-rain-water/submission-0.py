class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        start = 0
        end = 0
        leftmax = []
        rightmax = []
        for i in range(1, len(height) - 1):
            if height[i - 1] > start:
                start = height[i - 1]
                leftmax.append(start)
            else:
                leftmax.append(start)
            if height[len(height) - i] > end:
                end = height[len(height) - i]
                rightmax.append(end)
            else:
                rightmax.append(end)
        rightmax.reverse()
        final = 0
        for i in range(1, len(height)-1):
            a = leftmax[i-1]
            b = rightmax[i-1]
            if height[i] >= min(a, b):
                continue
            final += min(a, b) - height[i]
        return final

        