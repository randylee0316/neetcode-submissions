class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        new = {}

        for index, num in enumerate(nums):
            if target - num not in new:
                new[num] = index
            else:
                x = [new[target-num], index]
        return x
        