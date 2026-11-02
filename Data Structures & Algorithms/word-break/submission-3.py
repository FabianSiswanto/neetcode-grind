class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        right to left -> go from i = len(s) to 0 -> i = len(s) is true
        if current i match (dont forget to check bounds) 
            -> dp[i] = dp[i + len word (next word index)]
        '''
        n = len(s)

        # dp[i] -> if s[:i] can be segmented
        dp = [False] * (n + 1)
        # size n + 1 -> to make space for base case at 1 over last valid index -> n

        #base case
        dp[n] = True
        
        for i in range(n - 1, -1, -1):
            for word in wordDict:
                after_end_i = i + len(word)

                if after_end_i > n:
                    continue

                # check if word matches
                is_word_match = s[i: after_end_i] == word
                if is_word_match:
                    # propagate future word's status
                    dp[i] = dp[after_end_i] # check if future match too

                if dp[i]: # alr found match -> no need to go through other words again
                    break
        
        return dp[0]