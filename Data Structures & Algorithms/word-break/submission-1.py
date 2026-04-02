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
                in_bounds = i + len(word) <= n
                # check if word matches
                if in_bounds and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)] # check if future match too
                if dp[i]:
                    break
        
        return dp[0]