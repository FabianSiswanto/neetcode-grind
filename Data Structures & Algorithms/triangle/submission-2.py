class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        action: 
            other steps +
            min between:
            - row_index + 1 -> j + 1
            - row_index -> 

        dp[i - 1]

        dp[cur] = min(index - 1, index i, index i + 1) + dp(prev)

        dp[i, j] = min of 
        '''
        dp = [[0] * len(row) for row in triangle]

        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                val = triangle[i][j]

                if i == 0 and j == 0:
                    dp[i][j] = val
                elif j == 0:
                    dp[i][j] = val + dp[i - 1][j]
                elif j == len(triangle[i]) - 1: #bruh
                    dp[i][j] = val + dp[i - 1][j - 1]
                else: 
                    same_j = dp[i - 1][j]
                    diff_j = dp[i - 1][j - 1]
                    dp[i][j] = val + min(same_j, diff_j)

        return min(dp[-1])