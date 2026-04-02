class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        i, j are position

        actions:
        - move down
        - move right

        store num of paths

        dp[i][j] = 
        '''
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m): # row 
            for j in range(1, n): # col
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
        