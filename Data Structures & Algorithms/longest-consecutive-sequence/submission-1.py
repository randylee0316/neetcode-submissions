class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = {}
        nums = sorted(nums)

        for num in nums:
            if num -1 not in x:
                x[num] = 1
                continue
            x[num] = x[num-1] + 1
        y = 0
        for i in x.values():
            if i > y:
                y = i
        return y
        