class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set(["+", "-", "*", "/"])
        tokens.reverse()
        s = []
        while tokens:
            x = tokens.pop()
            if x not in operations:
                s.append(int(x))
            else:
                if x == "+":
                    a = s.pop()
                    b = s.pop()
                    s.append(b + a)
                elif x == "-":
                    a = s.pop()
                    b = s.pop()
                    s.append(b - a)
                elif x == "*":
                    a = s.pop()
                    b = s.pop()
                    s.append(b * a)
                else:
                    a = s.pop()
                    b = s.pop()
                    s.append(int(b/a))
        return s[-1] 


        