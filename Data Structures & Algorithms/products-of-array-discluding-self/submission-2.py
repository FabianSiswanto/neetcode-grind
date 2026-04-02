class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        - prefix -> 1 pass on res
        - suffix -> 1 pass on res -> opposite direction

        use multiplier that start with 1
        '''
        n = len(nums)
        res = [0] * n

        suffix_multiplier = 1
        for i in range(n - 1, -1, -1):
            res[i] = suffix_multiplier
            suffix_multiplier *= nums[i]

        prefix_multiplier = 1
        for i in range(n):
            res[i] *= prefix_multiplier
            prefix_multiplier *= nums[i]

        return res


        
