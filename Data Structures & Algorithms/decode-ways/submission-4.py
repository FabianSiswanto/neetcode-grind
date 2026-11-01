class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        solution:
        - invalid -> start with 0
        - self
        - self + next one

        dp[i]
        - invalid -> 0
        - take two -> if pass less than 26 check -> dp[i + 1] + dp[i + 2] -> two branches, dont overlap
        - standalone -> take from next one -> dp[i + 1]
        '''
        # dp = { len(s): 1}

        # for i in range(len(s) - 1, -1, -1):
        #     if s[i] == "0":
        #         dp[i] = 0
        #     elif i + 1 < len(s) and "10" <= s[i:i+2] <= "26":
        #         dp[i] = dp[i + 1] + dp[i + 2]
        #     else: # only standalone possible, one branches
        #         dp[i] = dp[i + 1]

        # return dp[0]

        one_ahead = 1 # base case
        two_ahead = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                cur = 0
            elif i + 1 < len(s) and "10" <= s[i:i+2] <= "26":
                cur = one_ahead + two_ahead
            else:
                cur = one_ahead
            
            # update state
            one_ahead, two_ahead = cur, one_ahead

        return one_ahead


        