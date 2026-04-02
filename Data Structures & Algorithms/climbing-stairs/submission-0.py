class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        actions:
        - climb 1 step
        - climb 2 step

        F(n) = F(n-1) + F(n-2)
        F(1) = F(0) = 1
        '''
        dp = [0] * (n + 1)

        for i in range(n + 1):
            if i == 0 or i == 1:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]