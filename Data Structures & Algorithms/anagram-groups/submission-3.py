class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            alpha = [0]*26
            for letter in word:
                i = ord(letter) - ord('a')
                alpha[i] += 1
            dic[tuple(alpha)].append(word)
        return list(dic.values())