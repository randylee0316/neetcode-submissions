class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False]*len(s)

        for i in range(len(s)):
            string = s[:i+1]
            if string in words:
                dp[i] = True
            else:
                for word in wordDict:
                    if len(word) > len(string):
                        continue
                    if string[-len(word):] == word:
                        dp[i] = dp[i-len(word)]
                        if dp[i] == True:
                            break
        
        return dp[-1]


                