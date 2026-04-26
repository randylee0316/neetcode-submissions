class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        f = [0]*len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                val, ind = stack.pop()
                f[ind] = i - ind
            stack.append((t, i))
        return f

        