class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for word in strs:
            alpha = [0]*26
            for letter in word:
                index = ord(letter) - ord('a')
                alpha[index] += 1
            dictionary[tuple(alpha)].append(word)
        
        return list(dictionary.values())
        