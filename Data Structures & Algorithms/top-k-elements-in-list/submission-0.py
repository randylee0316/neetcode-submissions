class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        lst = [[] for i in range(len(nums)+1)]

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1
        for key, values in dictionary.items():
            lst[values].append(key)
        final = []
        for i in lst[::-1]:
            for j in i:
                final.append(j)
                if len(final) == k:
                    return final


        