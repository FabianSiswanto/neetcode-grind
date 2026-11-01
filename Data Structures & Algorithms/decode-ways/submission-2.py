class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        dp[i]: two options
        - take 1 character -> keep at standalone -> dp[i + 1]
        - take 2 character -> combine with next number -> dp[i + 2]
        then do figure out how many ways we can decode the rest

        dp[i] -> num of decodings up to index i
        - can add possible variation if cur num and not last one -> 1 to 2
        
        dp[i]
        - dp[i - 1] + 1 if prev item * 10 + cur item is between 10 to 26
        - dpi[i - 1] other case
        - 0 if prev item if cur item is 0 and prev item is not 1 or 2

        solution:
        two options:
        - self
        - self + next one

        dp[i]
        - invalid -> 0
        - standalone -> take from next one -> dp[i + 1]
        - take two -> if pass less than 26 check -> dp[i + 1] + dp[i + 2] -> two branches, dont overlap
        '''
        dp = { len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            elif i + 1 < len(s) and "10" <= s[i:i+2] <= "26":
                dp[i] = dp[i + 1] + dp[i + 2]
            else: # only standalone possible, one branches
                dp[i] = dp[i + 1]

        return dp[0]


        