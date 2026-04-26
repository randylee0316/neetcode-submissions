class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        final = []
        a = 1
        b = 1
        for i in range(len(nums)):
            a *= nums[i]
            b *= nums[-i-1]
            prefix.append(a)
            suffix.append(b)
        suffix.reverse()
        for j in range(len(nums)):
            if j == 0:
                final.append(suffix[j + 1])
                continue
            elif j == len(nums) - 1:
                final.append(prefix[j-1])
                continue
            final.append(prefix[j-1]*suffix[j+1])
        return final

            
        