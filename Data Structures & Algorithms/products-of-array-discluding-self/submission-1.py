class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        final = []
        a = 1
        y = len(nums) - 1
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
                suffix.append(nums[y])
                continue
            x = nums[i]*prefix[i-1]
            prefix.append(x)
            j = nums[y - i]*suffix[i-1]
            suffix.append(j)
        for i in range(len(nums)):
            if i == 0:
                final.append(suffix[-2])
                continue
            if i == len(nums) - 1:
                final.append(prefix[-2])
                continue
            num = prefix[i-1]*suffix[-i-2]
            final.append(num)
        return final


            
        