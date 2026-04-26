class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        x = [[] for i in range(len(nums)+1)]

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1
        for key, value in dictionary.items():
            x[value].append(key)
        final = []
        for i in x[::-1]:
            for j in i:
                if len(final) < k:
                    final.append(j)
        return final


        