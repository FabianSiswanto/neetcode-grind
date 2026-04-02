class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        keep track of cumulative sum
        if with existing cur sum beban (curSum + num), just leave curSum (num only)
        '''
        curSum = 0
        maxSum = nums[0]
        for num in nums:
            curSum = max(curSum + num, num) # kalo curSum beban, just leave it
            # if curSum < 0:
            #     curSum = 0 # ditch day ones if they beban
            # curSum += num
            maxSum = max(curSum, maxSum)

        return maxSum
                
        