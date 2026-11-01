class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        dp[i] -> length of lis starting at index i

        go right to left
        base case -> dp[last index] = 1

        recursive case -> take max of:
        - 1
        - if cur < item in index to the right, j -> 1 + dp[j]
        '''
        dp = [1] * len(nums) # LIS starting at index 1

        for i in range(len(nums) - 1, -1, -1):
            # at base case, last index -> loop is empty -> will not run -> LIS is 1
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)