class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        dp[i] -> max money with index i of houses

        actions: (max between two options)
        - rob house -> cannot be adjacent -> self (cur val) nums[i] + dp[i - 2]
        - skip house -> dp[i - 1]

        base case:
        - dp[0] = cur_val
        - dp[1] = max(cur_val, dp[0])
        '''
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]
            
        dp = [None] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            money_rob = nums[i] + dp[i - 2]
            money_skip = dp[i - 1]
            dp[i] = max(money_rob, money_skip)

        return dp[-1]


        