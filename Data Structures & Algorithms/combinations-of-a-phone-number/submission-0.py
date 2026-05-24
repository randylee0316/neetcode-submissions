class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []

        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i,j,s):
            if j >= len(d[digits[i]]):
                return
            new = d[digits[i]][j]
            if i == len(digits)-1:
                res.append(s+new)
                return
            dfs(i+1, 0, s + new)
            dfs(i+1, 1, s+new)
            dfs(i+1, 2, s+new)
            dfs(i+1, 3, s+new)
        dfs(0,0, '')
        dfs(0, 1, '')
        dfs(0, 2, '')
        dfs(0, 3, '')
        
        return res

            
