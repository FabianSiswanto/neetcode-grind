class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        - two pointer -> left and right

        left_wall
        right_wall

        if cur > wall_h -> trigger h possible_h and wall_h
            else -> res += cur - wall_h


        process one side that is weaker
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
                res += left_wall - cur
            else: # right wall is higher
                r -= 1
                cur = height[r]

                right_wall = max(right_wall, cur)
                res += right_wall - cur

        return res