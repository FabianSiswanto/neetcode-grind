class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        action: 
            dp(i, j) = triangle(i, j) + min(
                        two options from prev row
                        - same j index: dp(i - 1, j)
                        - diff j index: dp(i - 1, j - 1)
                        )

        edge cases:
        - j cant be negative: j = 0 -> val + dp(i - 1, j)
        - j at the end of each row -> prev row dont have that index:
            j = len(triangle[i] - 1) -> val + dp(i - 1. j - 1)

        return min of last dp row
        '''
        dp = [[0] * len(row) for row in triangle]

        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                val = triangle[i][j]

                if i == 0 and j == 0:
                    dp[i][j] = val
                elif j == 0:
                    dp[i][j] = val + dp[i - 1][j]
                elif j == len(triangle[i]) - 1: #nature of triangle, upper row have less col
                    dp[i][j] = val + dp[i - 1][j - 1]
                else: 
                    same_j = dp[i - 1][j]
                    diff_j = dp[i - 1][j - 1]
                    dp[i][j] = val + min(same_j, diff_j)

        return min(dp[-1])