class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        final = [0]*len(temperatures)
        for index, value in enumerate(temperatures):
            while stack and stack[-1][1] < value:
                i, v = stack.pop() 
                d = index - i
                final[i] = d
            stack.append((index, value))
        return final


        