class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        f = [0]*len(temperatures)
        stack = []

        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                ind, val = stack.pop()
                f[ind] = i - ind
            stack.append((i, v))
        return f

        