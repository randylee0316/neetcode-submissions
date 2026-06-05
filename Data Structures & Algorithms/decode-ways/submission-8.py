class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        prev, curr = 1, 1

        for i in range(1, len(s)):
            new = 0

            if s[i] != '0':
                new += curr

            if 10 <= int(s[i-1:i+1]) <= 26:
                new += prev

            prev, curr = curr, new

        return curr