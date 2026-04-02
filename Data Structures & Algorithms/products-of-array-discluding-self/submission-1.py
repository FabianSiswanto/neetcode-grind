class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        - prefix
        - suffix

        at idx i -> multiply prefix i - 1 * suffix i + 1
        '''
        n = len(nums)
        suffix, res = [0] * n, [0] * n

        suffix_multiplier = 1
        for i in range(n - 1, -1, -1):
            res[i] = suffix_multiplier
            suffix_multiplier *= nums[i]

        prefix_multiplier = 1
        for i in range(n):
            res[i] *= prefix_multiplier
            prefix_multiplier *= nums[i]

        return res


        
