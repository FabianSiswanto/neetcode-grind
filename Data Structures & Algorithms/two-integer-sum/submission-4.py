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
        num_to_i = {}
        ans = []

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in num_to_i:
                remainder_i = num_to_i[remainder]
                
                return [remainder_i, i]
            else:
                num = nums[i]
                num_to_i[num] = i
            


            
        
        