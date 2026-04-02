class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        go from i = len(s) to 0 -> i = len(s) is truue
        if current i match -> dp[i] = dp[i + len word]
        '''
        n = len(s)
        dp = [False] * (n + 1)

        #base case
        dp[n] = True
        
        for i in range(n - 1, -1, -1):
            for word in wordDict:
                after_end_i = i + len(word)
                in_bounds = after_end_i <= n
                # check if word matches
                if in_bounds and s[i: after_end_i] == word:
                    dp[i] = dp[after_end_i] # check if future match too
                if dp[i]:
                    break
        
        return dp[0]