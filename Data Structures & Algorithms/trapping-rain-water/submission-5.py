class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        - two pointer -> left and right

        initialize them first -> as used in loop comparison to decide which to handle first
        - left_wall
        - right_wall

        trapped water height depends on left and right wall -> take shorter wall
        -> process weaker side first
            -> update index first -> as left and right wall inititalized before loop starts
            -> update height
            -> update res
        '''

        l = 0
        r = len(height) - 1

        left_wall = height[l]
        right_wall = height[r]

        res = 0

        while l < r:
            # use wall that is shorter
            if left_wall < right_wall:
                l += 1
                cur = height[l]

                left_wall = max(left_wall, cur)
                res += left_wall - cur #never be negative as did max above
            else: # right wall is higher
                r -= 1
                cur = height[r]

                right_wall = max(right_wall, cur)
                res += right_wall - cur

        return res