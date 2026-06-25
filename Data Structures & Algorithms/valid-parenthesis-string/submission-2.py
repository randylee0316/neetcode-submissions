class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                elif star:
                    star.pop()
        
        while left:
            if not star:
                return False
            if star[-1] > left[-1]:
                left.pop()
                star.pop()
            else:
                return False
        return not left

            
