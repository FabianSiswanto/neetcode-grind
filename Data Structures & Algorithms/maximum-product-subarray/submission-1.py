class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        store both cur min and cur max -> to make up for alternative (+/-)
        '''
        res = nums[0]
        cur_min, cur_max = 1, 1

        for num in nums:
            temp_min = num * cur_min
            temp_max = num * cur_max

            cur_max = max(temp_max, temp_min, num)
            cur_min = min(temp_max, temp_min, num)

            res = max(res, cur_max)

        return res
