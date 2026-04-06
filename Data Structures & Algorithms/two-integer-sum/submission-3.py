class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        dict:
        key: value
        num: index

        pass through
        check if remainder in dict
        if not build dict

        '''
        memo = {}
        ans = []

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in memo:
                remainder_i = memo[remainder]
                
                return [remainder_i, i]
            else:
                num = nums[i]
                memo[num] = i
            


            
        
        