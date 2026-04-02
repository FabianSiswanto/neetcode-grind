class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        sliding window leading with r
        keep track of cummulative sum
        if cur sum negative, increment l (remove negative prefix)

        '''
        curSum = 0
        maxSum = nums[0]
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num

            maxSum = max(curSum, maxSum)

        return maxSum
                
        