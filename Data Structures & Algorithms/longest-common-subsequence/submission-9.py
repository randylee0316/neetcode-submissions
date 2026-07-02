class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        if len(text1) > len(text2):
            text1, text2 = text2, text1
        
        dp = [0] * len(text1)

        for i in range(len(text2)):
            prev = 0
            for j in range(len(text1)):
                temp = dp[j]

                if text2[i] == text1[j]:
                    dp[j] = prev + 1
                else:
                    if j > 0:
                        dp[j] = max(dp[j], dp[j - 1])

                prev = temp

        return dp[-1]
                


                    
