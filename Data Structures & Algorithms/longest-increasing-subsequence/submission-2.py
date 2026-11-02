from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        dp[i] -> length of lis starting at index i
        -> go right to left
        base case -> dp[last index] = 1

        recursive case -> take max of:
        - 1
        - if cur < item in index to the right, j -> 1 + dp[j]
        '''
        dp = [1] * len(nums) # LIS starting at index 1

        for i in range(len(nums) - 1, -1, -1):
            # at base case, last index -> loop is empty -> will not run -> LIS is 1
            for j in range(i, len(nums)): #bottle neck
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

        '''
        for binary search to work -> need to do it in something sorted

        greedily keep tails with smallest values
        -> add new item if cur item is largest than last tails value
        -> if cur < last tails value
            -> find which index to replace
            -> replace item with that index -> keeps tails leanest it can be -> allows for the most extensions
        '''
        tails = [ nums[0] ]

        for i in range(1, len(nums)):
            num = nums[i]
            # check if can extend tail
            if tails[-1] < num:
                tails.append(num)
            else:
                idx_to_replace = bisect_left(tails, num)
                tails[idx_to_replace] = num

        return len(tails)
