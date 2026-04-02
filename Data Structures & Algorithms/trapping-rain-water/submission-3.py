class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        - two pointer -> left and right

        left_h
        right_h

        trapped water height depends on left and right wall -> take shorter wall
        -> process weaker side first
            -> update index
            -> update height
            -> update res
        '''

        l = 0
        r = len(height) - 1

        left_h = height[l]
        right_h = height[r]

        res = 0

        while l < r:
            # use wall that is shorter
            if left_h < right_h:
                l += 1
                cur = height[l]

                left_h = max(left_h, cur)
                res += left_h - cur #never be negative as did max above
            else: # right wall is higher
                r -= 1
                cur = height[r]

                right_h = max(right_h, cur)
                res += right_h - cur

        return res