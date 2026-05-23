class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        string = ""
        def backtrack(opened, closed):
            nonlocal res
            nonlocal string



            if opened == closed == n:
                res.append(string)
            
            copy = string

            if opened < n:
                string += '('
                backtrack(opened+1, closed)
            if closed < n and closed < opened:
                copy += ')'
                string = copy
                backtrack(opened, closed+1)
        
        backtrack(0, 0)

        return res

            

            

            