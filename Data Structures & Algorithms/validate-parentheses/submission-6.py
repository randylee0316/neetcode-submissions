class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        for i in s:
            if i == ")":
                if len(lst) == 0:
                    return False
                elif lst[-1] != "(":
                    return False
                else:
                    lst.pop()
            elif i == "}":
                if len(lst) == 0:
                    return False
                elif lst[-1] != "{":
                    return False
                else:
                    lst.pop()
            elif i == "]":
                if len(lst) == 0:
                    return False
                elif lst[-1] != "[":
                    return False
                else:
                    lst.pop()
            elif i == "(" or i == "{" or i == "[":
                lst.append(i)
        return len(lst) == 0
        
            

        