class Solution:

    def encode(self, strs: List[str]) -> str:
        x = ""
        for i in strs:
            x += str(len(i)) + "#" + i
        return x

    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        while i <= len(s) - 1:
            if s[i] == "#":
                i += 1
                continue
            x = ""
            while s[i] != "#":
                x += s[i]
                i += 1
            length = int(x)
            word = s[i+1:i+length+1]
            final.append(word)
            i = i+length+1
        return final


        
            


        
